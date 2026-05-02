# CAN 样例工程使用说明

本目录包含 CANoe 中经典的 CAN 总线协议系列样例配置工程，是学习 CANoe 最核心的基础模块。包含以下子工程：

## 1. Easy & Easy_Autosar
**功能简介**：
最基础的入门工程。`Easy` 仅包含两个简单的通信节点，演示最基础的报文收发、数据库绑定以及 Panel 控制。`Easy_Autosar` 则在此基础上加入了 Autosar 网络管理 (NM) 的概念演示。

## 2. CANSystemDemo & CANSystemDemo_Autosar
**功能简介**：
这是一个更为完整的 CAN 总线系统仿真演示，包含了多个节点（如引擎控制、仪表盘、车门控制等），逻辑更加复杂。`_Autosar` 后缀版本演示了基于 Autosar 标准的完整系统集成。

## 3. CAN_FD
**功能简介**：
演示 CAN FD (Flexible Data-rate) 的高级特性，包括大于 8 字节的数据负载以及可变波特率。

## 4. Diagnostics
**功能简介**：
演示汽车诊断功能（如 UDS 或 KWP2000），涵盖了诊断请求、响应、故障码(DTC)读取以及诊断控制台(Diagnostic Console) 的配合使用。

## 5. Scope
**功能简介**：
用于配合 Vector CAN Scope 硬件模块进行物理层波形分析的工程，适合排查物理层信号质量问题。

## 6. Stress
**功能简介**：
演示如何产生高总线负载、错误帧以及总线干扰（Bus Off），用于压力测试。

## 7. TestFeatureSet
**功能简介**：
演示基于 CANoe Test Feature Set (TFS) 进行自动化测试脚本 (XML/CAPL/C#) 编写和测试报告自动生成的综合实例。

## 8. MoreExamples
**功能简介**：
包含其他 CAN 相关的补充样例，诸如网关配置、部分网络(Partial Networking)等进阶特性的零散工程。

**使用说明**：
对于初学者，强烈建议从 `Easy` 目录下的工程开始学习；如果需要学习诊断或自动化测试，请依次打开 `Diagnostics` 和 `TestFeatureSet`。打开对应的 `.cfg` 文件并点击 Start 即可运行。
