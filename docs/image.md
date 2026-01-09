# 希沃镜像整理

本项目致力于整理和归档不同型号希沃一体机的系统镜像版本信息，为教育工作者和IT管理员提供参考。

## 📋 版本信息说明

希沃一体机的版本信息通常位于 `C:\Version\Version.txt` 文件中，包含以下关键信息：

- **设备型号**：如 MT71A-HX
- **硬件代次**：如 12&13代
- **操作系统**：Windows 版本和构建号
- **启动方式**：UEFI 或 Legacy
- **硬盘类型**：SATA 或 NVMe
- **架构位数**：64位 或 32位
- **希沃版本**：定制系统版本号
- **构建日期**：YYMMDD 格式

使用 [generate_md_from_txt.py](/cli/generate_md_from_txt.py) 范式化 `Version.txt` 内容

## 🗂 镜像档案

### MT71A 系列

<details>
<summary><b>MT71A-HX(12&13dai)-Win10ProUEFI(22H2)-SATA-64Bit-CHSEEWO(V7-A15.1)-240727</b></summary>

#### 基本信息
- **设备型号**: MT71A
- **硬件平台**: 
- **操作系统**: Windows 10 Professional 22H2 (UEFI启动)
- **系统架构**: 64位 SATA
- **希沃版本**: V7
- **构建日期**: 2024年7月27日

#### 预装软件清单

##### 核心教学软件
- `AirteachSetup_2.0.13.16752` - 希沃空中课堂
- `EasiNote5_Resource_20210923` - 希沃白板5资源包
- `EasiNoteSetup_5.2.3.824` - 希沃白板5

##### 外设支持
- `EasiCameraSetup_2.0.10.3855` - 希沃展台
- `EasiRecorderSetup_1.0.2.633` - 希沃录屏
- `SmartpenServiceSetup_2.0.1.755` - 智能笔服务

##### 系统工具
- `LifeCycleSetup_1.0.3.92` - 生命周期管理
- `SeewoIwbAssistant_0.0.3.1173` - 交互白板助手
- `SeewoLicenseSetup_2.0.2.192_factory` - 许可证管理
- `SeewoServiceSetup_1.4.6.3510` - 希沃服务

##### 投屏与协作
- `UniteActiveSetup_1.5.3.210` - 统一激活
- `大屏接收端SeewoPCAssistantPublicSetup_1.0.6.729` - PC助手公版
- `ScreenShareSuiteSetup_seewo_d_[282]_2.5.57.464` - 屏幕共享套件

##### 其他应用
- `W.P.S.20.2904(11.1.0.12763)` - WPS Office
- `EasiObservationSetup_1.0.2.629` - 希沃评课
- `EdulyseEdgeWindowsSetup_1.0.0.133` - Edulyse Edge
- `firewall_dns` - 防火墙DNS配置
- `SEEWO-FAMILY-BUCKET_NORMAL.7.0.0.10` - 希沃全家桶
- `UdiServerSetup_3.4.1.20` - UDI服务器

#### 备注
- V7-7dai
- V7第七代平台

</details>

<details>
<summary><b>MT71A-HX(12dai)-Win10ProUEFI(22H2)-SATA-64Bit-CHSEEWO-230723</b></summary>

#### 基本信息
- **设备型号**: MT71A
- **硬件平台**: 
- **操作系统**: Windows 10 Professional 22H2 (UEFI启动)
- **系统架构**: 64位 SATA
- **希沃版本**: 
- **构建日期**: 2023年7月23日

#### 预装软件清单

##### 核心教学软件
- `EasiNote5_Resource_20210923` - 希沃白板5资源包
- `EasiNoteSetup_5.2.2.9635_seewo` - 希沃白板5
- `SEEWO-FAMILY-BUCKET_EASINOTE.1.0.0.61` - 希沃全家桶

##### 外设支持
- `EasiCameraSetup_2.0.10.3829` - 希沃展台
- `EasiRecorderSetup_1.0.2.596` - 希沃录屏
- `SmartpenServiceSetup_1.0.1.349` - 智能笔服务

##### 系统工具
- `LifeCycleSetup_1.0.3.92` - 生命周期管理
- `SeewoIwbAssistant_0.0.3.1070` - 交互白板助手
- `SeewoLicenseSetup_2.0.2.187_factory` - 许可证管理
- `SeewoServiceSetup_1.3.4.3204` - 希沃服务

##### 投屏与协作
- `UniteActiveSetup_1.5.3.210` - 统一激活
- `大屏接收端SeewoPCAssistantPublicSetup_1.0.6.729` - PC助手公版
- `ScreenShareSuiteSetup_seewo_a_[154]_2.4.54.984` - 屏幕共享套件

##### 其他应用
- `EasiAgentSetup_0.0.1.130`
- `W.P.S.20.2904(11.1.0.12763)` - WPS Office
- `WifiFixSetup_1.0.4.103`

#### 备注

</details>

## 🔍 如何使用这些信息

1. **版本比对**: 对比当前系统版本与档案记录，确认是否需要更新
2. **故障排查**: 当某个功能异常时，可检查对应组件版本
3. **系统恢复**: 重装系统时确保安装正确版本的驱动程序和应用
4. **软件兼容性**: 确认第三方软件与当前系统版本的兼容性

## 📝 贡献指南

欢迎提交新的镜像版本信息！请确保：

- [ ] 提供完整的 `Version.txt` 内容
- [ ] 验证软件版本号的准确性  
- [ ] 注明设备型号和采集日期
- [ ] 不包含任何敏感信息或个人数据

## ⚠️ 免责声明

本档案仅用于技术参考和教育目的：
- 所有信息来源于公开渠道
- 软件版权归希沃及相关厂商所有
- 使用任何软件请遵守相关许可协议
- 不对因使用本信息造成的任何损失负责

---

*最后更新: $(date)*