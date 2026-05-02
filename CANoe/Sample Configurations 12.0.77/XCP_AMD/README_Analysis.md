# XCP_AMD 样例工程使用说明

本目录包含了基于 ASAM 标定协议（XCP/CCP）以及 AMD (AUTOSAR Monitoring and Debugging) 的 ECU 内部参数标定和测量仿真样例工程。

## 1. CCPSim
**功能简介**：
演示基于 CAN 总线的较早期标定协议 CCP (CAN Calibration Protocol)。展示如何通过 DAQ(Data Acquisition) 列表方式从 ECU 高速获取内部变量，以及对 ECU 内部存储器进行在线标定/修改。

## 2. XCP / XcpSim / XCP_FlexRay
**功能简介**：
展示了目前主流的 XCP (Universal Measurement and Calibration Protocol) 协议配置。XCP 是独立于物理层总线的，工程展示了：
- 基于 CAN 总线的 XCP。
- 基于 FlexRay 总线的 XCP。
- XcpSim 作为一个通用的仿真验证工程。
演示了对 ECU 内存地址（通常需提供 A2L 描述文件）直接读写的高级应用。

## 3. AMD
**功能简介**：
演示结合 AUTOSAR 架构的监测与调试特性 (AUTOSAR Monitoring and Debugging)。它常与 XCP 协议搭配，用于获取复杂 AUTOSAR 软件组件(SWC)、RTE 或 BSW 层的内部运行状态数据。

**使用说明**：
打开相应 `.cfg` 文件，需配合对应的 `.A2L` (ASAM MCD-2 MC) 数据库文件加载变量。打开 CANoe 提供的标定测量窗口或 Data Window，即可直观地获取模拟 ECU 内存的实时变化和曲线图形。
