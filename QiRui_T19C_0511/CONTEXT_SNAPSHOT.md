# QiRui_T19C_0511 会话快照（新开聊天用 @ 引用）

## CAPL 约束
- `/*@!Encoding:936*/`，注释 ASCII；禁 atof/atoi/sscanf；事件禁 return
- 禁 on signal_update / on signal 库名:: / this.phys
- 双 DBC sdadad+sdada：用 `$CAN1::报文::信号.phys`
- 规则：`.cursor/rules/capl-canoe-t19c.mdc`

## 已实现
- **IPClient.can**：UDP byte0/1/2 → `GW::VehicleSpeed` / `SteeringAngle` / `YawRate`
- **FCR_GW.can**：sysvar 变→写信号；50ms 定时器面板改信号→回写 sysvar
- 映射：VehicleSpeed↔ABS_ESP_1_VehicleSpeedVSOSig；SteeringAngle↔SAM_1_G；YawRate↔YAS_1
- MainTest：同上 + preStart/set_value_to_valid + crc.cin

## Git
- https://github.com/Huanghe5566/Vector_CANoe → `QiRui_T19C_0511/`，tag v1.0.0

## 待办（可选）
- IHU_11 事件 6 帧：改 DBC GenMsgNrOfRepetition 并 Trace 验证
