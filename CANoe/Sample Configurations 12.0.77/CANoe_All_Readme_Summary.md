# CANoe 样例工程综合使用说明 (All-in-One 汇总)

本文档将 `Sample Configurations 12.0.77` 目录下的 19 个协议与专题的 `README_Analysis.md` 进行了全局汇总。您可以直接在这一个文档中通过搜索快速查找到对应工程的功能与使用指引。

---

## 1. A429 样例工程使用说明

本目录包含 CANoe 中针对 ARINC 429 总线协议的样例配置工程。包括两个主要的工程：`A429System` 和 `A429BasicFDX`。

**A429System**：
该工程演示了典型的 ARINC 429 总线系统架构，包含基本的节点收发、数据库解析以及面板控制。包含数据库 (Database)、节点 (Nodes)、面板 (Panels)。
*使用说明*：直接在 CANoe 中打开 `A429System.cfg`，运行工程即可。

**A429BasicFDX**：
在基础系统上增加了 FDX (Fast Data eXchange) 功能，演示了如何通过外部客户端（C++ 或 C#）与 CANoe 进行高速数据交互。
*使用说明*：打开 `A429BasicFDX.cfg` 并运行，可编译并运行对应的 C# 或 C++ 客户端进行快速数据交换测试。

---

## 2. AFDX 样例工程使用说明

本目录包含针对 AFDX (Avionics Full-Duplex Switched Ethernet) 总线协议的样例配置工程。

- **AFDXBasic**：演示基础 AFDX 通信，包含常规的报文发送、接收、数据库配置及 CAPL 脚本控制。
- **AFDXBasicFDS**：演示 FDS (Functional Data Stream) 的配置，重点展示数据分段、组合及应用层数据映射。
- **AFDXBasicICMP**：演示 ICMP (如 Ping 操作) 在 AFDX 中的应用，用于网络连通性排查。
- **AFDXBasicIG**：演示通过 CANoe AFDX Interactive Generator 手动生成并发送报文。
- **AFDXManInTheMiddle**：演示中间人 (MitM) 仿真模式，配置网关拦截、修改或转发报文，适合安全性测试。

---

## 3. CAN 样例工程使用说明

本目录包含经典的 CAN 总线系列配置，是学习的最核心基础。

- **Easy & Easy_Autosar**：最基础的入门工程，仅含简单通信节点；后者增加了 Autosar 网络管理 (NM) 的概念。
- **CANSystemDemo & CANSystemDemo_Autosar**：完整的系统仿真演示（引擎、仪表盘等），后者基于 Autosar 标准集成。
- **CAN_FD**：演示 CAN FD 的高级特性（大于 8 字节负载、可变波特率）。
- **Diagnostics**：演示汽车诊断功能（UDS/KWP2000请求与 DTC 读取）。
- **Scope**：配合 CAN Scope 硬件模块进行物理层波形分析。
- **Stress**：演示产生高总线负载、错误帧及 Bus Off，用于压力测试。
- **TestFeatureSet**：演示基于 CANoe TFS 的自动化脚本测试与报告生成。

---

## 4. CANaero 样例工程使用说明

基于航空领域的 CAN 通信协议（如 ARINC 825）样例。

- **A825System**：完整的 ARINC 825 总线系统，包含数据库解析及飞行器系统数据仿真。
- **A825BasicTrafficGenerator**：A825 基础流量生成器，产生周期及事件性背景流量进行负载测试。
- **CANaeroBasicGalleySystem**：模拟航空器经典的厨房系统 (Galley System) 控制逻辑交互。
- **CANaeroBasicJoyStick**：演示外部真实操纵杆 (Joystick) 的输入与 CANoe 接入控制。

---

## 5. CANopen 样例工程使用说明

针对 CANopen 协议栈特性的演示。

- **CANopenSystem**：完整网络仿真系统，含 NMT 主从节点状态机交互。
- **CANopenBasicPDOGuarding**：演示 PDO 通信及 Node Guarding 节点保护机制。
- **CANopenBasicSDOTransfer**：演示 SDO 传输协议及读写对象字典操作。
- **CANopenBasicSafetyHeartbeat**：演示心跳报文机制 (Heartbeat) 用于在线监控。
- **CANopenGateway**：网络间的网关路由及数据映射。
- **Vector ProCANopen**：结合外部 ProCANopen 工具进行高级设计配置。

---

## 6. Car2x 样例工程使用说明

智能网联汽车（V2X / Car2x）通信样例。

- **Car2x_EU**：欧洲 ITS-G5 标准演示。含典型场景（CAM 合作感知和 DENM 分布式环境通知消息）。
- **Car2x_US**：美国 WAVE/DSRC 标准演示。演示 BSM 安全消息的收发解析与轨迹交互。
*使用说明*：结合 Map Window (地图窗口) 观察车辆位置移动及消息广播。

---

## 7. Ethernet 样例工程使用说明

车载以太网相关系统及协议演示。

- **Analysis**：报文抓包分析，Trace 中解析 IPv4/v6、TCP/UDP 以及 SOME/IP。
- **Diagnostics**：演示通过 DoIP 实现车载诊断及请求响应。
- **EthernetSystem**：基于 SOME/IP 协议的跨节点服务发现及通信调度综合仿真。
- **MoreExamples**：包含 AVB, TSN, MACsec 等前沿高级特性演示。
- **Simulation**：应用层模型仿真与以太网数据流建模传输。
- **Test**：通过 CAPL/C# 应用在以太网节点上的自动化测试。

---

## 8. FlexRay 样例工程使用说明

FlexRay 确定性高速车载总线协议。

- **FlexRaySystemDemo**：节点间的静态段/动态段通信交互的核心工程。
- **Autosar_NM_Demo / TP_PDU_Demo**：Autosar NM 及 TP/PDU 传输复用机制。
- **DiagnosticsTester**：演示不同传输层 (Autosar TP / ISO TP) 进行的诊断测试。
- **InCycleMuxDemo**：循环内复用 (同一个 ID 不同内容) 特性。
- **2Cluster_Gateway**：两个不同 FlexRay Cluster 集群间的路由转发。
- **Scope / CAPL_On_Board**：物理层眼图分析及将 CAPL 下发至板载硬件执行的范例。

---

## 9. IO_HIL 样例工程使用说明

CANoe 与外界交互的硬件在环 (HIL) 平台。

- **VTSystem**：与 Vector 官方 VT System 硬件配合进行引脚级故障注入及测控。
- **Matlab / LabVIEW**：通过接口与 Simulink 及 LabVIEW 建立模型和闭环仿真。
- **FMI**：将第三方 FMU 模型导入 CANoe 环境进行联合仿真。
- **XIL API**：通过 ASAM XIL 标准接口被外部自动化测试平台调取。
- **硬件接口通讯**：支持 GPIB, RS232, TCP_IP 及 GPS 定位数据直接通信采集。

---

## 10. ISO11783 样例工程使用说明

ISOBUS 农业及林业机械网络控制。

- **ISO11783SystemDemo**：拖拉机与农具间参数通信交互系统。
- **VirtualTerminalDemo**：演示 Virtual Terminal (虚拟终端) 中对象池(Object Pool) 的动态上载及即插即用显示。
- **ISO11783TestAutomation**：结合 TFS 进行 ISOBUS 功能和文件服务器的自动化测试。
- **GNSS**：集成卫星定位进行农机数据交互。

---

## 11. J1587 样例工程使用说明

商用车辆和重型车辆早期标准。

- **J1587SystemDemo**：通过 MID 识别网络节点及解析 PID 参数的应用演示。

---

## 12. J1939 样例工程使用说明

商用车辆及重卡核心 CAN 网络标准。

- **J1939SystemDemo / TruckOverview**：重型卡车 PGN 解析、宏观控制台、EMS/TCU/ABS 协调交互。
- **Diagnostics**：专属诊断报文 (如 DM1 的 DTCs 解析) 机制。
- **Modeling / TestFeatureSet**：支持引入复杂外部模型和标准商用车自动化测试。
- **BAM 机制**：包含地址声明及大包多包传输协议 (BAM/CMDT) 范例。

---

## 13. LIN 样例工程使用说明

LIN 总线（低速网络）协议与仿真。

- **LINSystem**：完整的主从节点系统演示，演示主节点调度表 (Schedule Table) 的轮询机制。
- **标准对比**：包含国际 ISO 17987 与美系 SAE J2602 的实施差异演示。
- **LINBasicStress / LINDiagnosticsTester**：物理层压力、总线干扰测试与 LIN 诊断传输测试。
- **一致性测试**：提供自动化脚本验证 LIN 从节点是否符合协议规范。

---

## 14. MOST 样例工程使用说明

车载信息娱乐系统高速光纤协议 (MOST)。

- **MOSTSystemDemo**：基于函数块 (FBlock) 架构的控制流机制（如电台/功放操作）。
- **MOSTStreaming**：演示 MOST 特有的音频同步流及连续流传输特性。
- **MOST_High_Protocol**：异步通道的高速大数据传输 (MHP / MEP)。
- **分析与外接**：通过 Scanner/Spy 监控底层环路锁、或通过 COM 接口对 MOST 仿真进行外部控制。

---

## 15. Programming 样例工程使用说明

CANoe 的跨语言接口和高级扩展。

- **自动化控制**：利用 C#, C++, Python 及 COM 接口实现远程控制 CANoe 和数据处理。
- **DLL 调用**：在 CAPL 脚本中调用定制 C/C++ DLL (如图像算法或音频驱动 MMSoundDll) 极大扩展功能。
- **BLF Logging**：基于脚本解析或生成离线 .BLF 报文记录文件。
- **二次开发框架**：演示利用 Visual Studio 创建 .NET 自动化测试库及面板控件 (ControlPlugin)。

---

## 16. SOA (面向服务架构) 样例工程使用说明

现代智能网联及软件定义汽车核心协议。

- **SOASystem**：基于 SOME/IP 实现的服务提供者 (Provider) 和消费者 (Consumer) 的发布/订阅互动体系。
- **SOABasicAsrAdaptive**：演示基于 AUTOSAR Adaptive (高性能计算平台) 中 ARA 架构服务通讯方法调用的集成方案。

---

## 17. Sensor 样例工程使用说明

汽车底层底盘及感知传感器专有通信方案。

- **SENT**：高精度高速单向点对点通信演示 (常见于节气门位置等)。
- **PSI5**：常用于高安全性环境(气囊传感器)的两线调制机制演示。
- **SPI**：微处理器与周边 SPI 外围芯片级的数字通讯。

---

## 18. SmartCharging 样例工程使用说明

新能源车与充电桩 (EVSE) 握手协议仿真。

- **GBT27930**：中国国家标准基于 CAN 总线的直流快充状态机及时序建立演示。
- **DIN70121_ISO15118**：欧美 CCS 联合充电系统标准，包括即插即充 (Plug & Charge)、底层 PLC 通信及加密验证机制。

---

## 19. XCP_AMD 样例工程使用说明

在线标定和变量读写标准。

- **CCPSim**：基于传统的 CAN 标定协议。
- **XCP (CAN / FlexRay)**：支持多种传输层的独立标定协议，配合 A2L 数据库可直接抓取和修改虚拟 ECU 内部参数。
- **AMD**：结合 AUTOSAR 架构特有的监控特性，实现对 SWC 或 RTE 层内部数据的探测。

---
> **总结提示**：
> 以上就是整个 `Sample Configurations` 目录中 19 个协议领域和技术专题的核心指南汇总。
> 在调用这些工程时，请保持原始文件的只读状态或进行副本备份。直接双击任何一处的 `.cfg` 文件即可快速体验其对应领域的领先技术架构。
