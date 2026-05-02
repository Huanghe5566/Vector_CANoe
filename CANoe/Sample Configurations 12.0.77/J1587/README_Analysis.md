# J1587 样例工程使用说明

本目录包含 CANoe 针对 SAE J1587（商用车辆和重型车辆早期标准）通信协议的演示样例。基于 J1708 物理层。

## 1. J1587SystemDemo
**功能简介**：
商用车辆 J1587 网络的标准系统级仿真演示。展示了如何通过 MID (Message Identification Character) 区分和识别网络上的节点（如引擎、制动系统等）以及解析 PID (Parameter Identification) 参数。

## 2. MoreExamples
**功能简介**：
包含其他关于 J1587 诊断、参数收发或跨协议网关的补充演示工程。

## 3. Database
**功能简介**：
定义了用于解析 J1587 参数和消息结构所需的 `.dbc` 数据库文件。

**使用说明**：
进入 `J1587SystemDemo` 目录，打开 `.cfg` 工程并运行即可。可在 Trace 窗口中清晰地观察到按照 J1587 标准解码的参数列表及物理层的调度行为。
