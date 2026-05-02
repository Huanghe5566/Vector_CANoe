# ISO11783 样例工程使用说明

本目录包含 CANoe 对于 ISO 11783（即 ISOBUS）农业及林业机械串行控制和通信协议标准的仿真样例工程。ISOBUS 本质上是 J1939 的扩展。

## 1. ISO11783SystemDemo
**功能简介**：
完整的 ISOBUS 系统演示。包含了拖拉机和不同农具（Implement）之间的多节点通信仿真，演示了设备工作参数（如 PTO、速度）的实时交互。

## 2. VirtualTerminalDemo
**功能简介**：
演示了 ISOBUS 体系下核心的 Virtual Terminal (VT，虚拟终端) 特性。该工程展示了拖拉机控制台终端界面如何从农具动态上传 Object Pool（对象池）从而实现界面的即插即用显示。

## 3. ISO11783TestAutomation
**功能简介**：
结合 CANoe Test Feature Set (TFS)，展示了如何编写自动化测试脚本对 ISOBUS 网络、VT 控制以及文件服务器等功能进行一键式验证并生成测试报告。

## 4. GNSS
**功能简介**：
演示了在 ISOBUS 网络中如何集成 GNSS/GPS 全球卫星导航系统的数据，模拟实现农业机械的精准定位数据交互。

## 5. MoreExamples
**功能简介**：
包含文件服务器(File Server)、任务控制器(Task Controller)等 ISOBUS 扩展特性的演示，适用于高级工程机械的开发。

**使用说明**：
打开对应的 `.cfg` 工程即可运行。建议从 `ISO11783SystemDemo` 结合 CANoe 的 ISOBUS/VT 交互窗口学习，能够直观看到虚拟界面的动态加载和刷新过程。
