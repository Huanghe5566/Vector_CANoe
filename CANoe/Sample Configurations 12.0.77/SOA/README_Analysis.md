# SOA (面向服务架构) 样例工程使用说明

本目录包含 CANoe 针对现代智能网联汽车 SOA (Service Oriented Architecture) 架构协议体系的配置演示。它是车载以太网和软件定义汽车的核心技术栈。

## 1. SOASystem
**功能简介**：
全面演示 SOA 架构的工程，通常基于 SOME/IP 通信协议构建。该示例展示了服务提供者 (Provider) 和服务消费者 (Consumer) 之间的动态服务发现、请求/响应(Request-Response) 以及事件订阅(Subscribe/Event)机制。不同于传统的面向信号(Signal)的静态通信，它展示了面向服务对象的数据交换。

## 2. SOABasicAsrAdaptive
**功能简介**：
基于 AUTOSAR Adaptive 平台架构的 SOA 系统演示。AUTOSAR Adaptive 是为高性能车载计算平台（如自动驾驶域控制器）量身定制的标准，此工程展示了 Adaptive AUTOSAR 环境中的应用层服务间通信和基于 ARA (AUTOSAR Runtime for Adaptive Applications) 标准的方法调用配置。

**使用说明**：
打开相应的 `.cfg` 工程即可运行。在仿真或网络监控中，推荐使用 CANoe 的 "Communication Concept" 配置窗口（而不是传统的数据库配置）和 Trace 窗口的服务发现视图来分析服务的发布与订阅过程。
