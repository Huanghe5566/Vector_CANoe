# IO_HIL 样例工程使用说明

本目录包含 CANoe 与各类外部 I/O 及硬件在环 (HIL) 测试平台交互的综合样例。

## 1. VTSystem
**功能简介**：
演示了 CANoe 与 Vector 官方的 VT System 硬件配合，进行引脚故障注入、模拟信号测控、继电器驱动等标准的 HIL 测试应用。

## 2. Matlab / LabVIEW
**功能简介**：
演示 CANoe 如何与 MATLAB/Simulink 以及 LabVIEW 建立模型级、信号级的联合仿真接口，执行复杂的闭环控制逻辑。

## 3. FMI (Functional Mock-up Interface)
**功能简介**：
展示了如何将第三方工具生成的 FMU 模型导入到 CANoe 环境中进行仿真联合与交互。

## 4. XIL API
**功能简介**：
通过 ASAM XIL API 标准接口控制 CANoe，演示如何从外部测试自动化平台调取 CANoe 的仿真资源。

## 5. 基础硬件接口及协议 (GPIB, RS232, TCP_IP, GPS)
**功能简介**：
包含了一系列使用底层协议栈与外部设备通信的例子：串口(RS232)、仪器仪表控制接口(GPIB)、基于网口及 TCP/IP 的套接字通信以及通过 GPS 模块获取真实的物理定位。

## 6. IO 扩展硬件 (IOCab, IOPiggy, IO_Hardware)
**功能简介**：
演示了通过 CANoe 支持的其他各类通用模拟/数字 IO 硬件板卡进行信号测量和激发的范例。

## 7. FDX (Fast Data eXchange)
**功能简介**：
提供 CANoe 与外部执行机进行快速数据交换机制的详细应用场景演示。

**使用说明**：
进入相关子目录后，需确保系统安装了对应的第三方驱动（如 MATLAB, LabVIEW 或 VT System 配置等）才能运行特定工程。对于纯软件联合仿真(如 Matlab)，只需打开 `.cfg` 文件并按照内部说明初始化 Simulink 模型即可。
