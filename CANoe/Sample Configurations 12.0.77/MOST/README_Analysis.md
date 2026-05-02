# MOST 样例工程使用说明

本目录包含 CANoe 针对车载信息娱乐系统高速光纤总线协议——MOST (Media Oriented Systems Transport) 的样例工程。

## 1. MOSTSystemDemo
**功能简介**：
基础的 MOST 系统演示。包含了基础控制流报文(Control Channel) 发送与解析、以及基于函数块(FBlock)架构的节点仿真，演示了常见的多媒体控制（如功放调节、电台切换）。

## 2. MOSTStreaming
**功能简介**：
演示 MOST 网络特有的同步流/音频流分配和数据传输 (Synchronous Data Channel) 特性，模拟音频或媒体数据的连续流传输。

## 3. MOST_High_Protocol / MOST_High_MultiConnection
**功能简介**：
演示了在 MOST 异步通道上基于 MOST High 协议 (MHP) 或以太网数据传输协议(MEP) 进行大容量数据通信或多重并发连接的管理与交互机制。

## 4. MOSTDiagnostics
**功能简介**：
展示了如何通过 MOST 协议封装车载诊断功能（DoMOST）与各多媒体节点进行诊断会话。

## 5. 高级分析及接口 (Scanner / Spy / COM_Clients)
**功能简介**：
- **Scanner / Spy**：演示如何对 MOST 环网进行底层状态监控(如 Ring Lock 等)、节点注册(Registry)及底层通讯抓取。
- **COM_Clients**：展示了如何通过 COM 接口（如通过外部脚本或程序）驱动和控制 CANoe 的 MOST 相关功能模块。

## 6. ECL (Electrical Control Line)
**功能简介**：
展示基于电气控制线的节点唤醒、休眠以及异常状态监控诊断机制的测试。

**使用说明**：
进入相关子目录并打开 `.cfg` 工程。仿真 MOST 通常需要 XML 格式的 Function Catalog 数据库，配合 CANoe 的 MOST Interactive Generator 能够非常方便地构建基于函数块的控制报文。
