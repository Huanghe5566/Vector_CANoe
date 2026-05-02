# A429 样例工程使用说明

本目录包含 CANoe 中针对 ARINC 429 总线协议的样例配置工程。包括两个主要的工程：`A429System` 和 `A429BasicFDX`。

## 1. A429System
**功能简介**：
该工程演示了典型的 ARINC 429 总线系统架构，包含基本的节点收发、数据库解析以及面板控制。
- **数据库 (Database)**：包含 `FCMS.dbc`, `Fuelsystem_Sensors1.dbc`, `Fuelsystem_Sensors2.dbc`, `OVHD_Panel.dbc`，定义了燃油系统传感器和头顶面板等报文。
- **节点 (Nodes)**：用于模拟 A429 总线上的数据收发节点。
- **面板 (Panels)**：提供了用户交互界面（如头顶面板），并通过 `.vsysvar` 系统变量与底层数据映射。

**使用说明**：
直接在 CANoe 中打开 `A429System.cfg`，运行工程即可通过面板操作和监控 A429 报文交互，适合学习 A429 基础解析。

## 2. A429BasicFDX
**功能简介**：
在 `A429System` 基础上增加了 FDX (Fast Data eXchange) 功能，演示了如何通过外部客户端（C++ 或 C#）与 CANoe 进行高速数据交互。
- **FDX 客户端**：包含 `FDXClient_C#` 和 `FDXClient_C++` 两个目录，内含与 CANoe 进行 FDX 通信的客户端源码。
- **FDX 描述文件**：`FDXDescription.xml`，用于定义 CANoe 和外部客户端交互的数据结构。

**使用说明**：
打开 `A429BasicFDX.cfg` 并运行。如需体验 FDX，可编译并运行对应的 C# 或 C++ 客户端，通过 FDX 接口与运行中的 CANoe 节点进行快速数据交换。适用于需要联合仿真的高级场景。
