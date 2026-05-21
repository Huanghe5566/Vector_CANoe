# QiRui_T19C_0511 会话快照（新开聊天用 @ 引用）

## CAPL 约束
- `/*@!Encoding:936*/`，注释 ASCII；禁 atof/atoi/sscanf；事件禁 return
- 禁 on signal_update / on signal 库名:: / this.phys
- 双 DBC sdadad+sdada：用 `$CAN1::报文::信号.phys`
- 规则：`.cursor/rules/capl-canoe-t19c.mdc`

## 已实现
- **IPClient.can**：UDP ASCII CSV `speed, steer, yaw` → `GW::VehicleSpeed` / `SteeringAngle` / `YawRate`（兼容 3 字节旧格式）
- **FCR_GW.can**：sysvar 变→写信号；50ms 定时器面板改信号→回写 sysvar
- 映射：VehicleSpeed↔ABS_ESP_1_VehicleSpeedVSOSig；SteeringAngle↔SAM_1_G；YawRate↔YAS_1
- MainTest：同上 + preStart/set_value_to_valid + crc.cin

## Git
- https://github.com/Huanghe5566/Vector_CANoe → `QiRui_T19C_0511/`，tag v1.0.0

## 事件开关 IHU_11
- `TriggerIhu11SwitchEvent(idx,...)`：`FCR_GW.can` / MainTest；sysvar `Vehicle_Input::EventSwitch::*`
- 信号：BSD / DVD_SET_DOW / DVD_SET_RCW / RCTBSwtSet / RAEBSwtSet（0/1/2/3）
- IL `applILTxPending(0x4FC)` 放行 3 帧
