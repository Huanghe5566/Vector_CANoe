# QiRui_T19C_0511 — 奇瑞 T19C CANoe 仿真测试工程

**版本**: V1.0.3  
**CANoe**: 12.0.221（配置见 `Chery_T19C.cfg` 文件头）

面向奇瑞 **T19C / RLCR / RRCR** 相关 CAN FD 网络的仿真与台架测试，集成 DBC、面板、系统变量及 CAPL 校验逻辑。

## 目录结构

| 路径 | 说明 |
|------|------|
| `Chery_T19C.cfg` | CANoe 主配置（双击或用 CANoe 打开） |
| `DBC/` | CAN FD 数据库（RLCR / RRCR / T19CEV 等） |
| `Code/` | CAPL/仿真代码：`FCR_GW.can`（网关侧 CRC/E2E 等）、`D01P_Vehicle_Message.can`（节点与报文故障注入相关）、`crc.cin` |
| `Code/MainTest/` | 测试分支用的 CAPL 变体 |
| `Panel/` | 面板：`Chery.xvp`、`Chery_T19C_Test.xvp`、`公CAN车身及报警测试.xvp` |
| `Sys/` | 系统变量：`SysvarChery.vsysvar`、`sys_2.vsysvar` |
| `Cdd/` | ECU 诊断描述（CDD）及迁移日志 |

## 使用说明

1. 安装 **Vector CANoe 12 SP**（与 cfg 中版本一致或兼容）。
2. 将整个工程目录放在本地固定路径（配置内 DBC/CDD 为相对路径）。
3. 打开 **`Chery_T19C.cfg`**，检查 Simulation Setup 中节点与通道是否与硬件一致。
4. 通过 **`Panel/`** 内面板注入车身、车机开关（如 `IHU_11`）、雷达相关信号；必要时在 **CAPL** 中扩展事件或报文行为。

## Python 自动化框架

`autotest/` 是新增的 pytest 主控框架，CANoe 仍作为台架底座，负责 CANFD DBC、Restbus、Trace/BLF 和 CAPL 底层辅助；Python 负责配置加载、用例编排、UDP 点云回灌、报警判定和报告输出。

离线自检：

```bash
python -m pytest
```

真实 CANoe 台架运行：

```bash
python -m pytest autotest/test_cases --real-canoe --junitxml reports/junit/t19c.xml
```

项目差异放在 `autotest/project_config/t19c_rlcr_rrcr.yaml`，场景放在 `autotest/scenario_library/`。后续换项目时优先新增配置和协议插件，不直接改测试用例。

## 事件型报文（车机开关等）

DBC 中对 `IHU_11` 等开关信号配置了 **OnChangeWithRepetition**（`GenMsgNrOfRepetition=3`、`GenMsgCycleTimeFast=100ms`），由 **CGW_T19C** 节点 IL 发送。CAPL（`FCR_GW.can`）支持：

- 面板直接改 `$CAN1::IHU_11::IHU_11_BSDSwitchSts`（0/1/2/3）
- 系统变量 `Vehicle_Input::EventSwitch::IHU_11_BSDSwitchSts`（改值即发）；`IHU_11_BSDSwitchSts_Fire=1` 可重复触发同值
- autotest `bsd_lca_rcta_switch: true` → 写 `IHU_11_BSDSwitchSts=1`（ON）

若 OEM 要求 6 帧而非 3 帧，改 DBC `GenMsgNrOfRepetition` 后 Trace 复核。

## 许可证与合规

- 工程内含主机厂 / Tier 提供的 **DBC、CDD** 等资产，**请勿**在未取得授权的情况下对外二次分发或用于商业用途。
- 本仓库用于 **Vector CANoe** 学习与项目归档；工具软件需遵循 Vector 许可协议。

## 变更记录

### V1.0.3

- 面板 `UdpClientData` 支持回灌数据路径：发送格式 `START <文件夹路径>`（仅支持英文路径），例如 `START C:\ReplayData\sample`。
- 新增 **停止回灌** 按钮（`UDP::UdpSendStop`），发送 `STOP` 指令终止回灌。
- `IPClient.can`：UDP 面板参数持久化至 `Code/IPClient.ini`；`SendUdpData` / `SendUdpStop` 封装发送逻辑。

### V1.0.2

- UDP 接收 ASCII CSV：`speed, steer, yaw`（如 `25.50, 10.25, 0.015`）解析至 `GW::VehicleSpeed` / `SteeringAngle` / `YawRate`；仍兼容 3 字节旧格式；8 字节结束帧忽略（`IPClient.can`）。
- `FCR_GW.can` / `MainTest/FCR_GW.can`：系统变量与 CAN 信号双向同步（`ABS_ESP_1_VehicleSpeedVSOSig`、`SAM_1_G::SteeringAngle`、`YAS_1::YawRate`），50 ms 定时器支持面板改信号回写。
- 工程清理：移除冗余 `D01P_Vehicle_Message.can`、`crc.cin`（MainTest 保留 `crc.cin`）。

### V1.0.1

- 添加了 UDP 数据接收功能。

### v1.0.0

- 初始归档：奇瑞 T19C 相关 CANoe 配置、DBC、面板、CAPL 与诊断描述。

---

## 在仓库中的位置

本工程位于：<https://github.com/Huanghe5566/Vector_CANoe> 的 **`QiRui_T19C_0511/`** 子目录。

检出标签：

```bash
git clone https://github.com/Huanghe5566/Vector_CANoe.git
cd Vector_CANoe
git checkout V1.0.3
```

在 Windows 上克隆完整仓库（含 Vector 示例的长路径）时建议启用：`git config --global core.longpaths true`。
