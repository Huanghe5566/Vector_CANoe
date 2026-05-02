# Car2x 样例工程使用说明

本目录包含 CANoe 针对智能网联汽车（V2X / Car2x）通信的样例配置工程。包括了目前世界上两种主要的通信标准：

## 1. Car2x_EU
**功能简介**：
基于欧洲 ITS-G5 标准的 Car2x 协议栈演示。包含了典型的欧洲 V2X 场景（如 CAM 合作感知消息和 DENM 分布式环境通知消息），以及车路协同、车辆间通信的仿真测试。

## 2. Car2x_US
**功能简介**：
基于美国 WAVE/DSRC (IEEE 1609.x) 标准的 Car2x 协议栈演示。演示了 BSM (Basic Safety Message) 的收发、解析及车辆轨迹仿真交互等美国场景标准。

**使用说明**：
在 CANoe 中打开工程后，可以打开 Map 窗口 (Map Window) 以及 Car2x Station Manager，通过可视化的方式观察仿真车辆在地图上的位置移动及消息广播过程。适合进行 V2X 协议栈的开发与验证。
