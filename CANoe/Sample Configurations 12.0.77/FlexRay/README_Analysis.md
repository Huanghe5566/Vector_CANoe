# FlexRay 样例工程使用说明

本目录包含针对 FlexRay 确定性高速车载总线协议的演示工程。涵盖了各种拓扑和协议栈演示。

## 1. FlexRaySystemDemo
**功能简介**：
经典的 FlexRay 完整系统演示，包含节点间的周期性数据交换（静态段）及事件数据交换（动态段），是学习 FlexRay 基础报文和配置的核心工程。

## 2. Autosar_NM_Demo / Autosar_TP_PDU_Demo
**功能简介**：
演示基于 Autosar 规范的 FlexRay 网络管理 (NM) 协议栈以及传输层 (TP) 与 PDU (Protocol Data Unit) 多路复用的传输机制。

## 3. DiagnosticsTester_Autosar_TP_PDU_Demo / DiagnosticsTester_ISO_TP_PDU_Demo
**功能简介**：
演示通过不同的传输层标准 (Autosar 传输层及 ISO 传输层) 进行 FlexRay 总线上的诊断测试 (DiagnosticsTester)。

## 4. ISO_TP_PDU_Demo
**功能简介**：
演示传统的 ISO TP (传输层) 协议规范在 FlexRay 报文分段与重组中的应用。

## 5. InCycleMuxDemo
**功能简介**：
展示了循环内复用 (In-Cycle Multiplexing) 的机制，即同一报文 ID 在同一个通信周期的不同时隙中发送不同内容的特性。

## 6. 2Cluster_Gateway
**功能简介**：
演示了在两个不同的 FlexRay Cluster (集群) 之间进行通信报文路由和数据转发的网关工程。

## 7. Scope
**功能简介**：
用于配合 Vector FlexRay Scope 硬件进行电气物理层的眼图、波形分析演示。

## 8. CAPL_On_Board
**功能简介**：
演示了将 CAPL 节点下发至具备硬件执行能力的 Vector 接口卡 (如 VN Interfaces) 执行的配置范例。

**使用说明**：
进入相关目录打开 `.cfg` 工程文件即可。FlexRay 配置强依赖 FIBEX 或 ARXML 数据库，本样例展示了如何无缝加载数据库并在 Trace 窗口监控静态段/动态段通信流。
