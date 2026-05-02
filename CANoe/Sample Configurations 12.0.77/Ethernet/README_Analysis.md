# Ethernet 样例工程使用说明

本目录包含车载以太网 (Automotive Ethernet) 相关的 CANoe 仿真样例工程。由于车载以太网技术复杂，CANoe 提供了不同维度层面的示例。

## 1. Analysis
**功能简介**：
偏向于以太网报文抓包及分析的工程，展示了如何在 Trace 窗口中解析以太网帧、IPv4/IPv6、TCP/UDP 以及 SOME/IP 等常见协议栈。

## 2. Diagnostics
**功能简介**：
演示通过以太网总线 (DoIP - Diagnostics over Internet Protocol) 实现车载诊断的功能。包含诊断请求发送与响应的解析。

## 3. EthernetSystem
**功能简介**：
完整的车载以太网系统级仿真工程，涵盖了基于 SOME/IP (Scalable service-Oriented MiddlewarE over IP) 协议的跨节点服务发现及通信调度。

## 4. MoreExamples
**功能简介**：
包含诸如 AVB (Audio Video Bridging)、TSN (Time-Sensitive Networking)、MACsec 等更多高级特性或单独的网关演示。

## 5. Simulation
**功能简介**：
以应用层模型仿真为主，包含通过以太网实现数据流建模及传输机制的基础范例。

## 6. Test
**功能简介**：
演示如何在以太网节点上应用自动化测试脚本 (CAPL/C#) 进行自动化测试验证。

**使用说明**：
以太网配置通常伴随着 ARXML 或 FIBEX 数据库文件。直接打开对应的 `.cfg` 文件运行即可。学习 SOME/IP 通信推荐从 `EthernetSystem` 开始。
