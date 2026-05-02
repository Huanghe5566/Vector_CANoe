# CAN / CAN FD / UDS Project Entrypoints

| Order | Entry | Purpose | Key files | Notes |
| --- | --- | --- | --- | --- |
| 1 | `Easy\Easy.cfg` | Minimal classic CAN introduction | `Easy\CANdb\easy.dbc`; `Easy\Nodes\engine.can`; `Easy\Nodes\display.can`; `Easy\Nodes\light.can` | Best first step for CAN signal and node basics. |
| 2 | `CANSystemDemo\CANSystemDemo.cfg` | Full classic CAN vehicle model | `CANSystemDemo\CANdb\PowerTrain.dbc`; `CANSystemDemo\CANdb\Comfort.dbc`; `CANSystemDemo\Nodes\Gateway.can`; `CANSystemDemo\TestSetup.tse` | Good baseline for gateway, TP objects, CDD use, and test setup. |
| 3 | `CAN_FD\CAN_FD_Powertrain.cfg` | CAN FD powertrain plus classic CAN comfort gateway | `CAN_FD\CANdb\CAN_FD_Powertrain.dbc`; `CAN_FD\CANdb\Comfort.dbc`; `CAN_FD\Nodes\CAN_FD_CAN_Gateway.can`; `CAN_FD\Nodes\TFS_CAPL_CAN_FD.can` | Main CAN FD sample. Use for DLC, payload, gateway, and automation study. |
| 4 | `CANSystemDemo_Autosar\CANSystem_HighRes_Autosar.cfg` | AUTOSAR-style full CAN system with NM observer | `CANSystemDemo_Autosar\Databases\Comfort.arxml`; `PowerTrain.arxml`; `Comfort_AsrNM33.INI`; `Powertrain_AsrNM33.INI`; `CAPL Includes\NM_Observer_Include.cin`; `Panels\NM_Tester.xvp` | Best integrated NM sample in the full vehicle demo. |
| 5 | `MoreExamples\Autosar_NM_Demo\ASRNm.cfg` or `ASRNm.stcfg` | Standalone AUTOSAR NM and partial networking demo | `CANdb\DemoAsrNM.dbc`; `CAN_AsrNM33.INI`; `Nodes\nodeA.can`; `Nodes\Gateway.can`; `Panels\NM_Control.xvp` | Best focused NM sample. Covers active/passive, Repeat Message, communication enable/disable, PN masks, and car wakeup. |
| 6 | `Diagnostics\UDSBasic\UDSBasic.cfg` | Minimal UDS tester and ECU simulation | `Diagnostics\UDSBasic\Cdd\UDS-ExampleEcu-5.0.2.cdd`; `Diagnostics\UDSBasic\Nodes\SimDiagECU.can`; `Diagnostics\UDSBasic\Tester\Tester.can`; `Diagnostics\UDSBasic\Tester\TestModule.can` | Best UDS CAPL starting point. |
| 7 | `Diagnostics\UDSSystem\UDSSystem.cfg` | Complete UDS system configuration | `Diagnostics\UDSSystem\CDD\UDS-ExampleEcu-5.0.3.cdd`; `Diagnostics\UDSSystem\Nodes\DoorFL.can`; `Diagnostics\UDSSystem\Nodes\DoorFR.can`; `Diagnostics\UDSSystem\CAPL_Includes\*.cin`; `Diagnostics\UDSSystem\Testunits\vTESTstudio_DiagTest.vtsoproj` | Main advanced UDS sample. Covers sessions, security, DIDs, download, fault memory, panels, and tests. |
| 8 | `TestFeatureSet\CentralLockingSystem\CANoe_Configuration\CentralLockingSystem.cfg` | CANoe Test Feature Set with NM and UDS-related regression material | `TestFeatureSet\CentralLockingSystem\DBs\SampleUDS.cdd`; `TestFeatureSet\CentralLockingSystem\DBs\NM.dbc`; `TestFeatureSet\CentralLockingSystem\DBs\comfort.dbc`; CAPL and vTESTstudio assets under the same tree | Use after understanding UDSSystem if the goal is automated regression. |
| 9 | `TestFeatureSet\SeatTest\CANoe_Configuration\SeatTest.cfg` | Seat control test feature set sample | `TestFeatureSet\SeatTest\DBs\Seat.dbc`; `TestFeatureSet\SeatTest\DBs\kwp2000-seat.cdd`; CAPL and vTESTstudio assets | Related diagnostics automation reference, but it is KWP-oriented rather than the main UDS path. |

## Opening Sequence

1. Open `Easy\Easy.cfg` and inspect `easy.dbc`.
2. Open `CANSystemDemo\CANSystemDemo.cfg` and inspect both `PowerTrain.dbc` and `Comfort.dbc`.
3. Open `CAN_FD\CAN_FD_Powertrain.cfg` and compare `CAN_FD_Powertrain.dbc` with the classic `Comfort.dbc`.
4. Open `CANSystemDemo_Autosar\CANSystem_HighRes_Autosar.cfg` to observe NM state integration in a full AUTOSAR-style demo.
5. Open `MoreExamples\Autosar_NM_Demo\ASRNm.cfg` for isolated AUTOSAR NM and partial networking behavior.
6. Open `Diagnostics\UDSBasic\UDSBasic.cfg` and step through `Tester.can` key handlers.
7. Open `Diagnostics\UDSSystem\UDSSystem.cfg` and use `DoorFL.can` as the primary ECU behavior map.

## Do Not Treat As Primary Entrypoints

- `Diagnostics\K-Line\KLineDemo.cfg`: useful as historical diagnostics context, but outside the main CAN UDS path.
- `MoreExamples\OSEK_TP_MultiChannel\OSEK_TP_MultiChannel.cfg`: useful transport protocol context, but not the core UDS sample.
- `Scope`, `Stress`, and `CANDisturbanceInterface` samples: useful for physical-layer or robustness investigations, not first-pass CAN FD/UDS learning.
- `MoreExamples\Autosar_Global_Time\AsrGlobalTime.cfg`: AUTOSAR-related, but it targets global time synchronization, not NM.
