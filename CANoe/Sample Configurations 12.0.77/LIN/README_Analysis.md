# LIN 样例工程使用说明

本目录包含 CANoe 针对 LIN (Local Interconnect Network) 总线的仿真与测试样例。

## 1. LINSystem
**功能简介**：
经典的 LIN 完整网络系统级演示。展示了 LIN 主节点(Master) 如何通过调度表(Schedule Table)轮询各个从节点(Slave)并获取/下发数据。

## 2. 协议标准演示 (LINBasicISO17987 / LINBasicSAEJ2602)
**功能简介**：
演示针对特定国际和地区标准的 LIN 通信实现。ISO 17987 是国际通用的现代 LIN 标准，而 SAE J2602 则常用于美系标准。展示了两者在参数配置和行为上的异同。

## 3. LINBasicTP / LINDiagnosticsTester
**功能简介**：
演示了 LIN 网络上的诊断传输层 (TP - Transport Protocol) 及如何作为诊断测试仪 (Diagnostics Tester) 向 LIN 节点发起诊断请求 (如节点配置、读取数据)。

## 4. LINBasicStress
**功能简介**：
演示在 LIN 网络上产生总线干扰、位错误(Bit error)、校验和错误等压力测试手段，以验证从节点/主节点的鲁棒性。

## 5. 一致性及自动化测试 (LINSlaveConformanceTest / LINTestSAEJ2602 / LINTestServiceLibrary)
**功能简介**：
演示了如何基于 CANoe 针对 LIN 从节点进行标准的一致性测试 (Conformance Test)，以验证设备是否完全遵从 LIN 协议规范。并包含相关测试服务库(Test Service Library) 的使用示例。

## 6. LINGateway
**功能简介**：
演示 LIN 网络与其他高速/中速总线（如 CAN）之间的数据网关和路由转换。

## 7. Scope
**功能简介**：
配合硬件示波器，展示 LIN 物理层的波形采集与信号质量分析。

**使用说明**：
打开相应的 `.cfg` 工程即可运行。通过 LDF (LIN Description File) 导入数据库后，可以在 CANoe 的 Interactive Generator (IG) 或 Schedule 表格控制界面中手动切换和触发特定的调度动作。
