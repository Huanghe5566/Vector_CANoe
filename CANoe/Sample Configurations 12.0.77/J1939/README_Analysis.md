# J1939 样例工程使用说明

本目录包含针对 SAE J1939 标准（商用车辆及重型卡车核心 CAN 标准）的丰富演示工程。

## 1. J1939SystemDemo / TruckOverview
**功能简介**：
展示了典型的重型卡车 J1939 完整通信网络，包含发动机控制单元(EMS)、变速箱控制单元(TCU)、防抱死系统(ABS) 等节点的协调交互及 PGN (Parameter Group Number) 数据解析。`TruckOverview` 提供了更宏观的卡车图形化综合控制台。

## 2. Diagnostics
**功能简介**：
演示 J1939 特有的诊断报文收发机制，包括对 DM1 (Active Diagnostic Trouble Codes) 到 DM32 等系列诊断消息(DTCs) 的仿真和监控处理。

## 3. TestFeatureSet
**功能简介**：
通过 TFS 提供针对 J1939 网络及诊断特性的自动化测试范例，展示了如何生成符合商用车诊断标准规范的测试报告。

## 4. Modeling
**功能简介**：
演示了在 J1939 网络中如何引入复杂的模型（可能包含 Simulink 等模型或物理模型）以实现高度逼真的节点动态响应仿真。

## 5. MoreExamples
**功能简介**：
包含诸如地址声明 (Address Claiming) 协议、网关处理以及大报文多包传输 (BAM/CMDT 协议) 等高级/特定机制的补充范例。

## 6. Database
**功能简介**：
存放了符合 J1939 标准规范的 PGN/SPN 定义数据库文件 (`.dbc`)。

**使用说明**：
J1939 工程强依赖于数据库。打开相应的 `.cfg` 后，可以从 J1939 Scanner 窗口监控节点在线状态及地址声明过程，并利用 Interactive Generator (IG) 或 Panel 直观地发送和观察特定 PGN。
