# CANaero 样例工程使用说明

本目录包含基于航空领域的 CAN 通信协议（如 ARINC 825 和一般的 CAN 航空电子规范）的 CANoe 样例工程。

## 1. A825System
**功能简介**：
演示了一个完整的 ARINC 825 总线系统（航空业 CAN 标准），包括节点定义、报文结构、数据库解析以及飞行器系统的数据仿真。

## 2. A825BasicTrafficGenerator
**功能简介**：
ARINC 825 的基础流量生成器，用于在总线上产生符合 A825 协议规范的周期性及事件性背景流量，方便在负载条件下测试特定节点。

## 3. CANaeroBasicGalleySystem
**功能简介**：
模拟了航空器内经典的厨房系统 (Galley System)。演示了典型的机舱内部控制逻辑和数据交互场景。

## 4. CANaeroBasicJoyStick
**功能简介**：
演示如何将外部的真实操纵杆 (Joystick) 与 CANoe 进行连接，并将其输入信号转换为 CANaero 总线上的控制报文。适合硬件在环测试 (HIL) 场景的入门学习。

**使用说明**：
打开对应子目录中的 `.cfg` 工程即可运行仿真。如果想了解 ARINC 825 协议的特性，建议重点学习 `A825System` 和 `A825BasicTrafficGenerator` 两个工程的 CAPL 源码及数据库结构。
