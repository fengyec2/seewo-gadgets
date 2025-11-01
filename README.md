# Seewo Gadgets 🛠️

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/fengyec2/seewo-gadgets/pulls)
[![GitHub Stars](https://img.shields.io/github/stars/fengyec2/seewo-gadgets?style=social)](https://github.com/fengyec2/seewo-gadgets/stargazers)

一个精心整理的、用于增强希沃一体机使用体验的实用小工具与资源合集。

> **请注意**: 本项目为非官方项目，由社区驱动。所有工具和资源的使用风险请自行承担。

---

## 目录

- [💻 自动化实践](#自动化实践)
- [✨ 特性](#特性)
- [🚀 快速开始](#快速开始)
- [📦 资源列表](#资源列表)
    - [脚本](#脚本)
    - [文档与教程](#文档与教程)
    - [配置文件](#配置文件)
- [🤝 如何贡献](#如何贡献)
- [📄 许可证](#许可证)
- [🙏 致谢](#致谢)

---

## 自动化实践

> 此部分内容均已在真实教学环境中检验过可行性

<details>
<summary><b> 一台成熟一体机应该具备的品质 </b></summary>

- **🕗 6:40**：自动开机（硬件实现）
- **🔔 指定课程前**：自动打开希沃白板
- **🕗 12:40**：自动打开午自习提醒，结束时关闭
- **🕗 13:30**：自动打开午休提醒，结束时关闭

<img src="docs/images/summer_auto.PNG" alt="午自习提醒" width="200" />

- **🕗 14:07**：自动打开某某音乐并开始播放（SMTC 实现）
- **🕗 14:27**：自动停止音乐播放（SMTC 实现）
- **🔔 自习课**：自动打开自习提醒，下课关闭

<img src="docs/images/all_auto.PNG" alt="自习提醒" width="200" />

- **🔔 周测**：自动打开考试提醒并启动倒计时，考试结束关闭

<img src="docs/images/week_exam_auto.PNG" alt="考试提醒" width="200" />

- **🔔 晚自习**：每节自习自动打开午晚自习提醒，结束时关闭
- **🕗 22:30**：自动关机

</details>

## 特性

*   **🆓 完全免费开源**: 所有工具和代码均开源，可自由使用和修改。
*   **📚 内容丰富**: 涵盖脚本、教程、配置等多种资源类型。
*   **🛡️ 安全透明**: 所有代码公开可查，避免恶意软件。
*   **🔧 即拿即用**: 提供清晰的说明，降低使用门槛。
*   **🌍 社区驱动**: 欢迎所有人的贡献，共同完善。

## 快速开始

1.  **浏览资源**: 点击进入上方的 [📦 资源列表](#资源列表) 找到你需要的工具。
2.  **查看说明**: 每个资源目录下都有详细的 `README.md` 文件，说明其功能和使用方法。
3.  **下载使用**: 根据说明下载脚本、文档或配置文件。
4.  **(高级用户) 参与贡献**: 如果你有好的工具或想法，请参阅 [🤝 如何贡献](#如何贡献)。

**⚠️ 重要提示**: 在运行任何脚本前，请务必阅读其说明，并在测试环境中确认无误后再用于生产环境。

## 资源列表

### 脚本

| 名称 | 语言 | 描述 | 维护状态 |
| :--- | :--- | :--- | :--- |
| [**SwitchTo-BuiltInAdapter.ps1**](./scripts/SwitchTo-BuiltInAdapter.ps1) | PowerShell | 禁用/启用指定网络适配器，杀死特定程序 | 🟡 一般 |
| [**SwitchTo-ExternalAdapter**](./scripts/SwitchTo-ExternalAdapter.ps1) | PowerShell | 禁用/启用指定网络适配器，启动特定程序 | 🟡 一般 |
| [**Start-ProcessWithArguments**](./scripts/SwitchTo-ExternalAdapter.ps1) | PowerShell | 传递参数启动指定程序 | 🟡 一般 |
| [**autorun_ppt**](./scripts/autorun_ppt.bat) | Batch | 批处理窗口显示倒计时后启动 .ppsx 自动放映 | ✅ 活跃 |
| [**killppt**](./scripts/killppt.bat) | Batch | 清理 WPS/Office PPT 相关进程 | 🟡 一般 |
| [**send_esc**](./scripts/send_esc.ahk) | AutoHotkey | 发送 ESC 键给焦点窗口 | ✅ 活跃 |
| [**terminate_ppt_through_COM.ps1**](./scripts/terminate_ppt_through_COM.ps1) | PowerShell | 通过 COM 通信保存并关闭正在放映的 PPT | ✅ 活跃 |
| [**terminate_ppt_through_COM.vbs**](./scripts/terminate_ppt_through_COM.vbs) | VBScript | 通过 COM 通信保存并关闭正在放映的 PPT（Windows 11 25H2 移除了对 VBS 脚本的支持） | ✅ 活跃 |
| [**clean_explorer_icon_temp**](./scripts/clean_explorer_icon_temp.bat) | Batch | 清理文件资源管理器图标缓存 | 🟡 一般 |

### 自动化应用

| 名称 | 开源 | 描述 |
| :--- | :--- | :--- |
| [**ClassIsland**](https://classisland.tech/) | ✅ | 自动化主体 |
| [**Hourglass**](https://chris.dziemborowicz.com/apps/hourglass/) | ✅ | 支持传递参数的计时器 |

### 其他应用

| 名称 | 开源 | 描述 |
| :--- | :--- | :--- |
| [**SeewoSplash**](https://github.com/fengyec2/custom-seewo-splash-screen) | ✅ | Fluent 风格的希沃白板启动图自定义工具 |
| [**PlaylistControl**](https://github.com/fengyec2/PlaylistControl) | ✅ | 记录 SMTC 信息 |

### 文档与教程

| 名称 | 格式 | 描述 |
| :--- | :--- | :--- |
| [**希沃镜像**](./docs/image.md) | Markdown | 整理了小部分希沃原厂镜像 |

<!-- ### 配置文件

| 名称 | 适用软件 | 描述 |
| :--- | :--- | :--- |
| [**OBS 直播场景配置**](./configs/obs-profile/) | OBS Studio | 针对希沃课堂直播优化好的 OBS 场景配置文件。 | -->

## 如何贡献

我们非常欢迎您的贡献！让这个仓库变得对更多人有用。

你可以通过以下方式参与：

1.  **分享工具**: 将你编写的好用脚本提交上来。
2.  **完善文档**: 修正错别字、补充说明、撰写新的教程。
3.  **反馈问题**: 在使用中遇到问题，请 [提交 Issue](https://github.com/fengyec2/seewo-gadgets/issues)。
4.  **提出建议**: 有好的想法？也欢迎通过 Issue 告诉我们。

**贡献流程：**
1.  Fork 本仓库。
2.  创建你的特性分支 (`git checkout -b feature/AmazingTool`)。
3.  提交你的更改 (`git commit -m 'Add some AmazingTool'`)。
4.  推送到分支 (`git push origin feature/AmazingTool`)。
5.  打开一个 Pull Request。

## 许可证

本项目内容采用 [知识共享 署名 4.0 国际 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.zh) 许可证进行许可。  
这意味着您可以自由地**分享**和**改编**这些内容，但必须给出**适当的署名**，并提供指向本许可证的链接。

## 致谢

感谢所有为这个项目贡献代码、文档和想法的朋友们！  
也感谢希沃为我们提供了优秀的硬件基础，让我们有机会在其之上创造更多可能。

---
<div align="center">
如果这个项目对你有帮助，请给它一个 ⭐️ ！ 这是对作者最大的鼓励。
</div>