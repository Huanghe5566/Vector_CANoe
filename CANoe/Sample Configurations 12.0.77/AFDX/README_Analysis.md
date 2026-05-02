# AFDX 样例工程使用说明

本目录包含 CANoe 中针对 AFDX (Avionics Full-Duplex Switched Ethernet) 总线协议的样例配置工程。包括以下子工程：

## 1. AFDXBasic
**功能简介**：
该工程演示了基础的 AFDX 网络通信，包含常规的报文发送、接收、数据库配置及 CAPL 脚本控制。
- 适合初步学习和验证 AFDX 报文的组成和基本交互。

## 2. AFDXBasicFDS
**功能简介**：
演示了在 AFDX 中 FDS (Functional Data Stream / Frame Descriptor) 的配置和使用，重点展示了数据分段、组合及应用层数据映射的高级功能。

## 3. AFDXBasicICMP
**功能简介**：
演示了在 AFDX 网络中 ICMP (Internet Control Message Protocol) 协议的应用（如 Ping 操作），用于网络连通性测试和故障排查模拟。

## 4. AFDXBasicIG
**功能简介**：
演示了通过 CANoe 中的 AFDX Interactive Generator (IG) 模块来手动或半自动地生成和发送 AFDX 报文，无需编写代码即可快速进行测试激励。

## 5. AFDXManInTheMiddle
**功能简介**：
演示了中间人 (Man-in-the-Middle, MitM) 仿真模式，该工程配置了一个网关节点，用于拦截、修改或转发两个 AFDX 节点间的通信，非常适合故障注入和安全性测试。

**使用说明**：
进入对应的子目录，双击打开对应的 `.cfg` 工程文件，结合自带的 Panel 或 Trace 窗口，即可运行和观察各种 AFDX 功能的仿真效果。
