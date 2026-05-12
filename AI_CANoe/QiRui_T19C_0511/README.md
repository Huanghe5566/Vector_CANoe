# QiRui_T19C_0511 — 奇瑞 T19C CANoe 仿真测试工程

**版本**: V1.0.1  
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

## 事件型报文（车机开关等）

DBC 中对部分车机开关信号配置了 **OnChangeWithRepetition** 及报文级 **`GenMsgNrOfRepetition`** 等属性，由 **Interaction Layer** 按数据库定义发送；若与 OEM 要求的帧数/间隔不一致，需在 DBC 或 CAPL 侧对齐后用手机帐或 Trace 复核。

## 许可证与合规

- 工程内含主机厂 / Tier 提供的 **DBC、CDD** 等资产，**请勿**在未取得授权的情况下对外二次分发或用于商业用途。
- 本仓库用于 **Vector CANoe** 学习与项目归档；工具软件需遵循 Vector 许可协议。

## 变更记录

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
git checkout V1.0.1
```

在 Windows 上克隆完整仓库（含 Vector 示例的长路径）时建议启用：`git config --global core.longpaths true`。
