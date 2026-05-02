# Programming 样例工程使用说明

本目录包含 CANoe 与各类编程语言接口及高级二次开发自动化特性的演示工程。这些示例是进行 CANoe 集成开发与平台拓展的核心资源。

## 1. 自动化接口 (COM_Automation / COMDotNet / Python)
**功能简介**：
展示了如何通过外部编程语言（C#、C++、Python、VBScript 等）调用 CANoe 的 COM 接口，实现诸如启动/停止测量、设置变量、读取信号等外部远程自动化控制功能。

## 2. 动态链接库调用 (CAPLdll / C_Library / MMSoundDll / Bitmap_Library)
**功能简介**：
演示如何在 CAPL 脚本中调用外部开发的 C/C++ 动态链接库(DLL)。如调用音频文件播放 (`MMSoundDll`)、图形库处理以及复杂的算法逻辑。这极大扩展了 CAPL 的局限性。

## 3. 插件开发 (MenuPlugin / ControlPlugin)
**功能简介**：
展示如何通过 CANoe SDK 开发自定义的菜单项(Menu)以及在面板(Panel) 中嵌入自定义的用户控件(Control)。适用于为客户深度定制专属 UI 界面。

## 4. BLF 日志处理 (BLF_Logging)
**功能简介**：
演示如何通过编程方式对 CANoe 专有的日志文件格式 (.BLF) 进行解析、修改或生成，适用于后期数据离线分析处理脚本的开发。

## 5. 测试与刷写 (VS_DotNetTestLibary_Template / vFlashAutomation)
**功能简介**：
- **VS_DotNetTestLibary_Template**：提供了在 Visual Studio 中开发基于 .NET 的 CANoe 自动化测试库(C#)的工程模板。
- **vFlashAutomation**：演示了如何通过 CANoe 调用 vFlash 工具实现 ECU 自动化程序刷写。

**使用说明**：
不同工程需要配合特定的 IDE（如 Visual Studio 或 Python 环境）。运行前请阅读对应子目录内的注释文档或 readme，配置好运行环境（如注册 DLL，修改 COM 配置），再启动执行脚本或程序。
