# CAN / CAN FD / UDS CAPL Function Index

## Classic CAN

| File | Role | Key behavior |
| --- | --- | --- |
| `Easy\Nodes\engine.can` | Minimal engine simulation | Use with `easy.dbc` to understand simple CAN node signal behavior. |
| `Easy\Nodes\display.can` | Minimal display node | Use with `engine.can` to trace basic CAN signal flow. |
| `Easy\Nodes\light.can` | Minimal light node | Use with `LightState` messages in `easy.dbc`. |
| `CANSystemDemo\Nodes\Gateway.can` | Classic CAN gateway | Baseline for comparing classic CAN routing with CAN FD gateway routing. |
| `CANSystemDemo\Testmodul\EngineTester.can` | Classic CAN test module | Useful for learning CANoe test module structure before CAN FD and UDS tests. |
| `CANSystemDemo\Testmodul\TestCaseLibrary.can` | Shared classic CAN tests | Reusable test-case pattern reference. |

## Network Management

| File | Role | Key behavior |
| --- | --- | --- |
| `CANSystemDemo\Nodes\NM_Tester_C.can` | Classic comfort-bus NM tester/observer | Observes `CAN1.0x401-0x440`, maps NM ID from CAN ID offset, decodes command byte values into `ALIVE`, `RING`, `SLEEP_IND`, and `SLEEP_ACK`, then updates `NMTester` system variables and panel indicators. |
| `CANSystemDemo\Nodes\NM_Tester_PT.can` | Classic powertrain-bus NM tester/observer | Observes `CAN2.0x500-0x540`, tracks gateway and engine NM states, receiver IDs, sleep indication, sleep acknowledge, wakeup display, and bus communication activity. |
| `CANSystemDemo_Autosar\CAPL Includes\NM_Observer_Include.cin` | AUTOSAR NM state observer | Uses bus contexts for `Comfort` and `PowerTrain`, disables automatic NM/IL startup, reads local node IDs, maps `Nm_GetState()` to readable states, and refreshes panel state through `Nm_StateChangeNotification`. |
| `MoreExamples\Autosar_NM_Demo\Nodes\nodeA.can` | Representative AUTOSAR NM node | Demonstrates `Nm_SetVerbosity`, `Nm_SetAutoStartParam`, state indications, Repeat Message, passive/active mode, communication enable/disable, partial networking, user data, control bit vector, bus synchronization, detected node display, and car wakeup handling. Nodes B-D follow the same design pattern. |
| `MoreExamples\Autosar_NM_Demo\Nodes\Gateway.can` | AUTOSAR NM gateway and PN request controller | Aggregates panel requests for PN1/PN2, calls `Nm_SetPnRequestBits`, `Nm_NetworkRequest`, `Nm_NetworkRelease`, and controls the car wakeup bit. Best reference for partial networking gateway behavior. |

## CAN FD

| File | Role | Key behavior |
| --- | --- | --- |
| `CAN_FD\Nodes\CAN_FD_CAN_Gateway.can` | CAN FD to classic CAN gateway | `on message EngineData` routes CAN FD data to classic CAN `Gateway_2`; `on message Gateway_2` routes classic CAN speed to CAN FD `ABSdata`; `on signal ... Gear` routes one comfort signal into CAN FD gear signals. |
| `CAN_FD\Nodes\TFS_CAPL_CAN_FD.can` | CAN FD automated test module | `MainTest()` calls message wait, invalid DLC, signal change, DLC set/reset, and cycle-time test cases. Uses `testWaitForMessage`, `ChkStart_InconsistentDLC`, `testSetMsgDlc`, and cycle-time check APIs. |
| `CAN_FD\Send.can` | CAN FD send helper | Small helper node used by the configuration. Inspect when tracing generated CAN FD traffic. |
| `CAN_FD\Test.can` | CAN FD test helper | Small helper node used by the configuration. Inspect with `TFS_CAPL_CAN_FD.can` if test behavior is unclear. |

## UDSBasic

| File | Role | Key behavior |
| --- | --- | --- |
| `Diagnostics\UDSBasic\Nodes\SimDiagECU.can` | Minimal simulated UDS ECU | Handles `Door.Variant_Coding_Write`, `Door.EcuIdentification_Write`, `Door.Variant_Coding_Read`, `Door.EcuIdentification_Read`, and `Door.SeedLevel_0x01_Request`. Demonstrates `diagResponse`, `GetParameter`, `GetParameterRaw`, `SetParameter`, `SetParameterRaw`, positive response, and NRC responses. |
| `Diagnostics\UDSBasic\Tester\Tester.can` | Minimal diagnostic tester | Key handlers create `DiagRequest` objects, set parameters, send requests, and process `on diagResponse` callbacks. Shows positive/negative response checks and access modes. |
| `Diagnostics\UDSBasic\Tester\TestModule.can` | Minimal diagnostic test module | Use after `Tester.can` to learn how UDS request/response logic moves from manual key control to test automation. |

## UDSSystem ECU Nodes

| File | Role | Key behavior |
| --- | --- | --- |
| `Diagnostics\UDSSystem\Nodes\DoorFL.can` | Main full UDS ECU simulation | Includes diagnostic definitions, fault memory, and download simulation. Handles tester present, sessions, security access, DIDs, variant coding, ECU identification, periodic data, dynamic DIDs, IO control, communication control, ECU reset, download state, and system-variable reactions. |
| `Diagnostics\UDSSystem\Nodes\DoorFR.can` | Smaller UDS ECU simulation | Handles tester present, sessions, development data, serial number, ECU identification, ECU reset, and fault-memory related system variables. Use as a simplified contrast to `DoorFL.can`. |
| `Diagnostics\UDSSystem\Nodes\TesterPanelControl.can` | Tester panel controller | Bridges panel/system-variable operations to tester behavior. Inspect when panel actions are part of a diagnostic workflow. |

## UDSSystem Includes

| File | Role | Key behavior |
| --- | --- | --- |
| `Diagnostics\UDSSystem\CAPL_Includes\DiagDefinitions.cin` | Shared constants | Defines common NRC constants, parameter access modes, fault-memory type enum, periodic DID send modes, and application timeout. |
| `Diagnostics\UDSSystem\CAPL_Includes\FaultMemory_Sim.cin` | Fault memory simulation | Supports DTC/fault-memory state and GUI-related fault-memory behavior used by `DoorFL.can` and `DoorFR.can`. |
| `Diagnostics\UDSSystem\CAPL_Includes\Download_Sim.cin` | ECU-side download simulation | Supports request-download and transfer-data style ECU simulation. |
| `Diagnostics\UDSSystem\CAPL_Includes\Download_Tester.cin` | Tester-side download helper | Supports tester-side download flow and validation. |
| `Diagnostics\UDSSystem\CAPL_Includes\LibFunctions_Tester.cin` | Tester helper library | Reusable helper routines for diagnostic test sequences. |

## UDSSystem Test Modules

| File | Role | Key behavior |
| --- | --- | --- |
| `Diagnostics\UDSSystem\Testmodules\CAPL_Testcases_ECU1.can` | CAPL diagnostic test cases | Broad UDS regression coverage. Use together with `XML_Tester_ECU1.vxt` and vTESTstudio assets. |
| `Diagnostics\UDSSystem\Testmodules\XML_Tester_ECU1.vxt` | XML diagnostic test module | XML-based test module counterpart for UDSSystem. |
| `Diagnostics\UDSSystem\Testunits\DiagTest\DiagTest.vtt` | vTESTstudio diagnostic test unit | Test unit artifact. Open from vTESTstudio if you need structured test design. |

## High-Value API Patterns

- Message observation: `testWaitForMessage`, `TestGetWaitEventMsgData`, `testJoinMessageEvent`.
- CAN FD DLC checks: `ChkStart_InconsistentDLC`, `ChkStart_InconsistentTxDLC`, `ChkStart_InconsistentRxDLC`, `testSetMsgDlc`, `testResetMsgDlc`.
- CAN FD cycle checks: `ChkStart_MsgRelCycleTimeViolation`, `ChkStart_MsgAbsCycleTimeViolation`, `ChkStart_SignalCycleTimeViolation`.
- Classic NM observation: monitor NM CAN ID ranges, decode NM command bytes, update system variables, and clear wakeup/bus activity indicators with timers.
- AUTOSAR NM APIs: `Nm_SetAutoStartParam`, `Nm_GetState`, `Nm_StateChangeNotification`, `Nm_NetworkRequest`, `Nm_NetworkRelease`, `Nm_RepeatMessageRequest`, `Nm_EnableCommunication`, `Nm_DisableCommunication`, `Nm_EnablePartialNetworking`, `Nm_DisablePartialNetworking`, `Nm_SetPnRequestBits`, `Nm_SetCarWakeUpBit`.
- UDS ECU side: `on diagRequest`, `diagResponse`, `SendPositiveResponse`, `SendNegativeResponse`, `SetParameter`, `SetParameterRaw`.
- UDS tester side: `DiagRequest`, `SendRequest`, `on diagResponse`, `IsPositiveResponse`, `GetResponseCode`, `GetParameter`, `GetParameterRaw`.
