#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_md_from_txt.py
读取指定的 txt 文件，解析设备头部信息与预装软件列表，生成规范的 Markdown 文本（包含 <details> 折叠块）。
用法：
    python generate_md_from_txt.py input.txt [-o output.md]

行为说明：
- 第一行（首个非空行）被视为 header，例如：
  MT71A-HX(12&13dai)-Win10ProUEFI(22H2)-SATA-64Bit-CHSEEWO(V7-A15.1)-240727
- 中间若干行为软件列表（每行为一个条目）。
- 最后一行如果是像 "V7-7dai" 之类的额外备注，会放在备注中。
- 通过关键字映射将常见软件映射为中文描述，无法映射的条目保留原名但仍放入“其他应用”中。
"""

import re
import sys
import argparse
from datetime import datetime

# 简单的中文描述映射（可扩展）
DESCRIPTION_MAP = {
    "Airteach": "希沃空中课堂",
    "EasiNoteSetup": "希沃白板5",
    "EasiNote5_Resource": "希沃白板5资源包",
    "EasiCamera": "希沃展台",
    "SmartpenService": "智能笔服务",
    "EasiRecorder": "希沃录屏",
    "SeewoServiceSetup": "希沃服务",
    "SeewoLicenseSetup": "许可证管理",
    "LifeCycleSetup": "生命周期管理",
    "SeewoIwbAssistant": "交互白板助手",
    "ScreenShareSuite": "屏幕共享套件",
    "SeewoPCAssistantPublicSetup": "PC助手公版",
    "UniteActiveSetup": "统一激活",
    "W.P.S.": "WPS Office",
    "EasiObservation": "希沃评课",
    "EdulyseEdgeWindowsSetup": "Edulyse Edge",
    "UdiServerSetup": "UDI服务器",
    "SEEWO-FAMILY-BUCKET": "希沃全家桶",
    "firewall_dns": "防火墙DNS配置",
    # 备用通配
    "EasiNote": "希沃白板5",
    "EasiCameraSetup": "希沃展台",
    "Smartpen": "智能笔服务",
    "AirteachSetup": "希沃空中课堂",
}

# 分类关键词到分组名
CATEGORY_RULES = {
    "核心教学软件": ["Airteach", "EasiNote", "EasiNote5_Resource", "EasiNoteSetup", "AirteachSetup"],
    "外设支持": ["EasiCamera", "Smartpen", "EasiRecorder", "EasiCameraSetup", "SmartpenService", "EasiRecorderSetup"],
    "系统工具": ["SeewoService", "SeewoLicense", "LifeCycle", "SeewoIwbAssistant", "SeewoServiceSetup", "SeewoLicenseSetup", "LifeCycleSetup", "SeewoIwbAssistant_"],
    "投屏与协作": ["ScreenShare", "SeewoPCAssistant", "UniteActive", "ScreenShareSuite", "SeewoPCAssistantPublicSetup", "UniteActiveSetup"],
    "其他应用": ["W.P.S.", "EasiObservation", "EdulyseEdge", "UdiServer", "SEEWO-FAMILY-BUCKET", "firewall_dns"],
}

def smart_description(name: str) -> str:
    # 返回中文描述（尽量用映射），否则返回空字符串
    for key, desc in DESCRIPTION_MAP.items():
        if key.lower() in name.lower():
            return desc
    return ""

def categorize(name: str) -> str:
    for cat, keys in CATEGORY_RULES.items():
        for k in keys:
            if k.lower() in name.lower():
                return cat
    return "其他应用"

def parse_header(line: str) -> dict:
    """
    尝试从 header 中抽取字段：
    - device_model
    - hardware_platform (例如 第12&13代处理器)
    - os_name (例如 Windows 10 Professional)
    - os_version (例如 22H2)
    - boot (UEFI / BIOS)
    - arch (64位)
    - storage (SATA / NVMe / ...)
    - seewo_version (V7-A15.1)
    - build_date (yyyy-mm-dd / human readable)
    """
    info = {
        "device_model": "",
        "hardware_platform": "",
        "os_name": "",
        "os_version": "",
        "boot": "",
        "arch": "",
        "storage": "",
        "seewo_version": "",
        "build_date": "",
    }
    # 把 - 作为分隔
    parts = [p.strip() for p in line.split('-') if p.strip()]
    # model: 通常在第一个部分，且可能含有括号
    if parts:
        first = parts[0]
        # model：取第一个 '(' 前的内容，如果没有则全取
        m = re.split(r'[\(\[]', first)[0].strip()
        info["device_model"] = m

        # 如果第一部分含括号，尝试提取硬件平台
        hp = re.search(r'\(([^)]+)\)', first)
        if hp:
            hp_text = hp.group(1)
            # 将 dai/代 统一
            hp_text = hp_text.replace("dai", "代").replace("dài", "代")
            info["hardware_platform"] = hp_text

    # 逐段解析其他信息
    for p in parts[1:]:
        # OS + 版本 + UEFI
        if re.search(r'win', p, re.I):
            # 检查 UEFI
            if re.search(r'uefi', p, re.I):
                info["boot"] = "UEFI启动"
            # 版本括号
            v = re.search(r'\(([^)]+)\)', p)
            if v:
                info["os_version"] = v.group(1)
            # OS 名称规范化
            if re.search(r'win10', p, re.I):
                info["os_name"] = "Windows 10 Professional"
            elif re.search(r'win11', p, re.I):
                info["os_name"] = "Windows 11"
            else:
                # 直接把段落作为名称的粗略替代
                info["os_name"] = p
            continue

        # 存储接口或架构
        if re.search(r'\bSATA\b', p, re.I):
            info["storage"] = "SATA"
            # 可能同时有 64Bit
            if re.search(r'64', p):
                info["arch"] = "64位"
            else:
                # 如果包含 Bit
                b = re.search(r'(\d+)\s*Bit', p, re.I)
                if b:
                    info["arch"] = f'{b.group(1)}位'
            continue
        if re.search(r'(\d+)\s*Bit', p, re.I) and not info["arch"]:
            b = re.search(r'(\d+)\s*Bit', p, re.I)
            info["arch"] = f'{b.group(1)}位'
            continue

        # 希沃版本
        sv = re.search(r'V\d[\w\.\-\_]*', p, re.I)
        if sv:
            info["seewo_version"] = sv.group(0)
            continue
        # 也许在括号内：CHSEEWO(V7-A15.1)
        sv2 = re.search(r'\((V[\d\w\.\-]+)\)', p, re.I)
        if sv2:
            info["seewo_version"] = sv2.group(1)
            continue

        # 可能是日期
        date_match = re.search(r'(\d{6,8})$', p)
        if date_match:
            date_str = date_match.group(1)
            parsed = parse_date_token(date_str)
            if parsed:
                info["build_date"] = parsed
            else:
                info["build_date"] = date_str
            continue

        # 单独出现的日期段（纯数字）
        if re.fullmatch(r'\d{6,8}', p):
            parsed = parse_date_token(p)
            if parsed:
                info["build_date"] = parsed
            continue

    # 如果 header 最末尾就是裸日期（例如最后一个用 '-' 分开的部分）
    if not info["build_date"]:
        last_token = parts[-1] if parts else ""
        if re.fullmatch(r'\d{6,8}', last_token):
            parsed = parse_date_token(last_token)
            if parsed:
                info["build_date"] = parsed

    # 保底处理：如果 arch 未识别，但 header 中包含 "64"
    if not info["arch"] and re.search(r'64', line):
        info["arch"] = "64位"

    return info

def parse_date_token(tok: str) -> str:
    # 支持 YYMMDD 或 YYYYMMDD
    tok = tok.strip()
    try:
        if len(tok) == 6:
            # assume YYMMDD -> 20YY
            dt = datetime.strptime(tok, "%y%m%d")
        elif len(tok) == 8:
            dt = datetime.strptime(tok, "%Y%m%d")
        else:
            return ""
        # 返回 "YYYY年M月D日" 格式，移除前导0
        return f"{dt.year}年{dt.month}月{dt.day}日"
    except Exception:
        return ""

def parse_lines(lines):
    # 过滤空行并去掉 BOM
    lines = [l.strip() for l in lines if l and l.strip()]
    if not lines:
        return None
    header = lines[0]
    maybe_footer = ""
    if len(lines) >= 2:
        # 如果最后一行像 "V7-7dai" 或 "V7-7代" 之类，作为备注
        last = lines[-1]
        if re.match(r'^[Vv]\d[\w\-\_&\s]*\d*[dD]ai|^[Vv]\d', last) or re.search(r'\d代', last) or re.search(r'v\d', last, re.I):
            maybe_footer = last
            software = lines[1:-1]
        else:
            software = lines[1:]
    else:
        software = []

    return header, software, maybe_footer

def build_markdown(header_info: dict, header_raw: str, software_list: list, extra_note: str) -> str:
    md = []
    md.append("<details>")
    md.append(f"<summary><b>{escape_html(header_raw)}</b></summary>")
    md.append("")
    md.append("#### 基本信息")
    md.append(f"- **设备型号**: {header_info.get('device_model','')}")
    hp = header_info.get("hardware_platform")
    if hp:
        # 将 12&13代 形式美化
        hp = hp.replace("&", "&").replace("dai", "代")
        md.append(f"- **硬件平台**: 第{hp}处理器" if re.match(r'^\d', hp) else f"- **硬件平台**: {hp}")
    else:
        md.append(f"- **硬件平台**: ")

    os_name = header_info.get("os_name","")
    os_version = header_info.get("os_version","")
    boot = header_info.get("boot","")
    os_line = os_name
    if os_version:
        os_line += f" {os_version}"
    if boot:
        os_line += f" ({boot})"
    md.append(f"- **操作系统**: {os_line.strip()}")

    arch = header_info.get("arch","")
    storage = header_info.get("storage","")
    arch_storage = " ".join([x for x in [arch, storage] if x])
    md.append(f"- **系统架构**: {arch_storage}")

    seewo = header_info.get("seewo_version","")
    md.append(f"- **希沃版本**: {seewo}")

    build_date = header_info.get("build_date","")
    md.append(f"- **构建日期**: {build_date}")
    md.append("")

    md.append("#### 预装软件清单")
    md.append("")

    # 分类
    categories = {}
    for s in software_list:
        cat = categorize(s)
        categories.setdefault(cat, []).append(s)

    # 输出顺序： 按示例优先顺序
    order = ["核心教学软件", "外设支持", "系统工具", "投屏与协作", "其他应用"]
    for cat in order:
        items = categories.get(cat, [])
        if not items:
            continue
        md.append(f"##### {cat}")
        for it in items:
            desc = smart_description(it)
            desc_txt = f" - {desc}" if desc else ""
            md.append(f"- `{it}`{desc_txt}")
        md.append("")  # 分组之间空行

    md.append("#### 备注")
    if extra_note:
        md.append(f"- {extra_note}")
    else:
        if header_info.get("hardware_platform"):
            hp_text = header_info.get("hardware_platform").replace("dai", "代")
            md.append(f"- 适用于{hp_text}的{header_info.get('device_model')}")
    if seewo:
        md.append(f"- {seewo}第七代平台" if seewo.lower().startswith('v7') else f"- {seewo} 平台")
    md.append("")
    md.append("</details>")

    return "\n".join(md)

def escape_html(text: str) -> str:
    # 简单转义 < 和 >
    return text.replace("<", "&lt;").replace(">", "&gt;")

def main():
    parser = argparse.ArgumentParser(description="从 txt 解析设备与软件列表并生成 Markdown。")
    parser.add_argument("input", help="输入 txt 文件路径（UTF-8 编码）")
    parser.add_argument("-o", "--output", help="输出 md 文件路径（默认 stdout）", default=None)
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        raw_lines = [ln.rstrip("\n") for ln in f]

    parsed = parse_lines(raw_lines)
    if not parsed:
        print("未能解析到内容。", file=sys.stderr)
        sys.exit(2)
    header_raw, software_list, extra_note = parsed

    header_info = parse_header(header_raw)
    # 如果 header_info 没有 build_date，尝试从 header_raw 末尾取 6/8 位数字
    if not header_info.get("build_date"):
        m = re.search(r'(\d{6,8})$', header_raw)
        if m:
            header_info["build_date"] = parse_date_token(m.group(1))

    md = build_markdown(header_info, header_raw, software_list, extra_note)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"已生成 {args.output}")
    else:
        print(md)

if __name__ == "__main__":
    main()