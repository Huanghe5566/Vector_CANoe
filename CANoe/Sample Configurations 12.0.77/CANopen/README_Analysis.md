# CANopen 样例工程使用说明

本目录包含 CANoe 针对 CANopen 协议栈特性的演示样例工程。

## 1. CANopenSystem
**功能简介**：
完整的 CANopen 网络仿真系统，包含基础配置以及 NMT (Network Management) 的主从节点状态机交互演示。

## 2. CANopenBasicPDOGuarding
**功能简介**：
着重演示 CANopen 协议中的 PDO (Process Data Object) 通信以及 Node Guarding (节点保护) 监控机制。

## 3. CANopenBasicSDOTransfer
**功能简介**：
演示 SDO (Service Data Object) 传输协议，包含读写对象字典操作（Expedited, Segmented 传输模式等）。

## 4. CANopenBasicSafetyHeartbeat
**功能简介**：
演示 CANopen 安全协议中的 Heartbeat (心跳报文) 产生及消费机制，用于替代 Guarding 进行节点在线监控。

## 5. CANopenGateway
**功能简介**：
演示了 CANopen 网络与其他网络（如 CAN 网络）之间的网关路由及数据映射功能。

## 6. Vector ProCANopen
**功能简介**：
结合 Vector ProCANopen 工具的集成演示，展现了如何在 CANoe 配合下进行 CANopen 网络的高级设计与配置。

**使用说明**：
进入相应的子目录，打开 `.cfg` 文件即可运行。如需深入理解 CANopen 协议机制，可结合 CANoe 的 CANopen 配置窗口及对象字典进行查看。
