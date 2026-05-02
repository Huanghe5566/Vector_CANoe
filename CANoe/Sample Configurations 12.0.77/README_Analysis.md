# CANoe 样例工程总览与调用索引

本目录 (`Sample Configurations 12.0.77`) 包含 Vector CANoe 提供的丰富的通信协议和总线仿真验证工程样例。
为方便后期快速调用学习，我们对该根目录下的 19 个主要协议和专题目录进行了独立分析，并在各目录下生成了专属的 `README_Analysis.md` 说明文件。以下是总体索引及导读，共完成了 20 个整理任务。

## 目录索引与学习导图

1. **[A429](./A429/README_Analysis.md)**
   - 航空电子 ARINC 429 总线协议演示。
2. **[AFDX](./AFDX/README_Analysis.md)**
   - 航空电子全双工交换以太网基础及中间人网络攻击演示。
3. **[CAN](./CAN/README_Analysis.md)**
   - 最经典的 CAN/CAN FD 总线基础工程，强烈推荐初学者从这里的 `Easy` 目录入门。
4. **[CANaero](./CANaero/README_Analysis.md)**
   - 基于航空业标准（如 ARINC 825）的 CAN 变种总线系统。
5. **[CANopen](./CANopen/README_Analysis.md)**
   - 面向工业和自动化领域，涵盖 PDO、SDO 传输机制及网络节点管理。
6. **[Car2x](./Car2x/README_Analysis.md)**
   - 智能网联 V2X 专题，涵盖欧洲(ITS-G5)与美国(WAVE/DSRC)双通信标准。
7. **[Ethernet](./Ethernet/README_Analysis.md)**
   - 车载以太网应用前沿。包含 SOME/IP 系统、Diagnostics over IP 以及报文级仿真。
8. **[FlexRay](./FlexRay/README_Analysis.md)**
   - 高确定性、高带宽的 FlexRay 网络、In-Cycle 级复用和诊断支持演示。
9. **[IO_HIL](./IO_HIL/README_Analysis.md)**
   - 硬件在环测试与外部设备接口总览，涵盖 VT System、Matlab/Simulink 等软硬件联合仿真。
10. **[ISO11783](./ISO11783/README_Analysis.md)**
    - 基于 ISOBUS 的农林机械控制标准，包含独特的虚拟终端 (Virtual Terminal) 界面下发。
11. **[J1587](./J1587/README_Analysis.md)**
    - 经典商用车与重卡的 J1587(J1708) 数据总线网络分析。
12. **[J1939](./J1939/README_Analysis.md)**
    - 商用车及卡车领域主流配置，涵盖 PGN 解析及专属诊断系统。
13. **[LIN](./LIN/README_Analysis.md)**
    - 低成本车载网络，涵盖 LDF 解析、主从节点调度表轮询机制及一致性测试。
14. **[MOST](./MOST/README_Analysis.md)**
    - 高速车载多媒体光纤通信网络，演示同步流控制、音频流和 FBlock 功能模块。
15. **[Programming](./Programming/README_Analysis.md)**
    - 高级开发与扩展！演示了如何用 C#、Python、DLL 以及插件二次开发扩展 CANoe 的能力。
16. **[SOA](./SOA/README_Analysis.md)**
    - 面向服务的现代软件架构演示，特别是结合 AUTOSAR Adaptive 的服务订阅发布流。
17. **[Sensor](./Sensor/README_Analysis.md)**
    - 车载底层传感器物理通信仿真，包括 SENT、PSI5、SPI 接口协议。
18. **[SmartCharging](./SmartCharging/README_Analysis.md)**
    - 新能源汽车关键应用！涵盖国标(GB/T 27930) 及欧美标(ISO 15118)的充电握手协议模拟。
19. **[XCP_AMD](./XCP_AMD/README_Analysis.md)**
    - 基于 ASAM 标准对 ECU 内部存储及变量参数进行在线标定和测量的演示。

## 使用指引
- 每个目录下的 `README_Analysis.md` 包含该总线协议的具体应用场景及推荐的学习路径。
- **调用建议**：若要查找如何实现特定功能（如网关、测试脚本自动化），可进入对应的总线目录（如 CAN、Ethernet、LIN）寻找 `Gateway` 或 `TestFeatureSet` 子工程，直接双击 `.cfg` 文件进行启动和调用，无需修改原有代码。

---
> 备注：以上所有分析总结仅提取了设计意图及调用方法，全程未修改工程源码，保证了样例的原生可运行状态。
