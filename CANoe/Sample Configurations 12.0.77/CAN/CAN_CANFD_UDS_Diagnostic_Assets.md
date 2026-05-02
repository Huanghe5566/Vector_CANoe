# CAN / CAN FD / UDS Diagnostic Asset Index

## Network Management Assets

| Asset | Path | Purpose |
| --- | --- | --- |
| Classic NM tester DBC | `CANSystemDemo\CANdb\NM_Tester.dbc` | DBC for classic NM tester visualization in `CANSystemDemo`. |
| Classic comfort NM tester | `CANSystemDemo\Nodes\NM_Tester_C.can` | Observes comfort bus NM frames, decodes ALIVE/RING/SLEEP_IND/SLEEP_ACK, and updates `NMTester` system variables. |
| Classic powertrain NM tester | `CANSystemDemo\Nodes\NM_Tester_PT.can` | Observes powertrain bus NM frames and updates powertrain NM display system variables. |
| NM system variables | `CANSystemDemo\SystemVariables\NMTester.xml` | System variable namespace backing the classic NM tester panels. |
| AUTOSAR full-system NM config | `CANSystemDemo_Autosar\Comfort_AsrNM33.INI`; `Powertrain_AsrNM33.INI` | AUTOSAR NM node-layer configuration for the full vehicle demo. |
| AUTOSAR NM observer include | `CANSystemDemo_Autosar\CAPL Includes\NM_Observer_Include.cin` | Shared observer logic for displaying AUTOSAR NM state across Comfort and PowerTrain bus contexts. |
| AUTOSAR NM panel | `CANSystemDemo_Autosar\Panels\NM_Tester.xvp` | Panel for NM state visualization in the AUTOSAR full-system demo. |
| Standalone AUTOSAR NM project | `MoreExamples\Autosar_NM_Demo\ASRNm.cfg`; `ASRNm.stcfg` | Focused AUTOSAR NM sample entrypoints. |
| Standalone AUTOSAR NM DBC | `MoreExamples\Autosar_NM_Demo\CANdb\DemoAsrNM.dbc` | Database for the standalone AUTOSAR NM demo. |
| Standalone AUTOSAR NM config | `MoreExamples\Autosar_NM_Demo\CAN_AsrNM33.INI` | Defines car wakeup, PN settings, timing, node PN masks, and PN names. |
| Standalone AUTOSAR NM nodes | `MoreExamples\Autosar_NM_Demo\Nodes\nodeA.can`; `nodeB.can`; `nodeC.can`; `nodeD.can`; `Gateway.can` | Node behavior for active/passive mode, Repeat Message, communication control, PN request bits, car wakeup, and detected-node display. |
| Standalone AUTOSAR NM panels | `MoreExamples\Autosar_NM_Demo\Panels\NM_Control.xvp`; `NodeA.xvp`; `NodeB.xvp`; `NodeC.xvp`; `NodeD.xvp`; `Gateway.xvp` | Panels for controlling NM node state, PN requests, user data, control bits, and gateway wakeup behavior. |
| TestFeatureSet NM DBC | `TestFeatureSet\CentralLockingSystem\DBs\NM.dbc` | NM database used by the central locking test feature set sample. |

## UDSBasic Assets

| Asset | Path | Purpose |
| --- | --- | --- |
| CDD | `Diagnostics\UDSBasic\Cdd\UDS-ExampleEcu-5.0.2.cdd` | Diagnostic description used by the minimal UDS ECU/tester sample. |
| ECU CAPL | `Diagnostics\UDSBasic\Nodes\SimDiagECU.can` | Simulated ECU behavior for variant coding, ECU identification, and a negative-response seed request. |
| Tester CAPL | `Diagnostics\UDSBasic\Tester\Tester.can` | Manual tester behavior driven by keyboard input. |
| Test module | `Diagnostics\UDSBasic\Tester\TestModule.can` | Automated diagnostic test-module version of the basic tester flow. |

## UDSSystem Diagnostic Descriptions

| Asset | Path | Purpose |
| --- | --- | --- |
| CDD | `Diagnostics\UDSSystem\CDD\UDS-ExampleEcu-5.0.3.cdd` | Main CANoe diagnostic description for the UDSSystem sample. |
| PDX | `Diagnostics\UDSSystem\PDX\UDS-ExampleEcu-5.0.2.pdx` | PDX diagnostic package reference. Useful when studying ODX/PDX based diagnostics. |
| Additional description | `Diagnostics\UDSSystem\BasicDiagnostics\AdditionalDescription.xml` | Additional XML description used by the UDSSystem configuration. |

## UDSSystem ECU and Tester CAPL

| Asset | Path | Purpose |
| --- | --- | --- |
| Main ECU | `Diagnostics\UDSSystem\Nodes\DoorFL.can` | Full-featured simulated ECU. Primary implementation for sessions, security, DIDs, dynamic/periodic data, IO control, download, reset, and fault memory. |
| Secondary ECU | `Diagnostics\UDSSystem\Nodes\DoorFR.can` | Smaller ECU model. Useful contrast against `DoorFL.can`. |
| Tester panel control | `Diagnostics\UDSSystem\Nodes\TesterPanelControl.can` | Connects tester panel/system-variable operations to diagnostic actions. |
| Test cases | `Diagnostics\UDSSystem\Testmodules\CAPL_Testcases_ECU1.can` | CAPL diagnostic regression test cases for ECU1. |

## UDSSystem CAPL Includes

| Asset | Path | Purpose |
| --- | --- | --- |
| Diagnostic definitions | `Diagnostics\UDSSystem\CAPL_Includes\DiagDefinitions.cin` | Shared NRC constants, parameter access modes, fault-memory enum, periodic DID modes, and timeout constants. |
| Fault memory simulation | `Diagnostics\UDSSystem\CAPL_Includes\FaultMemory_Sim.cin` | Simulates DTC/fault memory behavior and related state. |
| ECU download simulation | `Diagnostics\UDSSystem\CAPL_Includes\Download_Sim.cin` | ECU-side implementation support for download/transfer flows. |
| Tester download support | `Diagnostics\UDSSystem\CAPL_Includes\Download_Tester.cin` | Tester-side helper logic for download workflows. |
| Tester helper library | `Diagnostics\UDSSystem\CAPL_Includes\LibFunctions_Tester.cin` | Shared helper routines for diagnostic test sequences. |

## Security Access

| Asset | Path | Purpose |
| --- | --- | --- |
| Seed/key DLL | `Diagnostics\UDSSystem\SecurityAccess\SeednKey.dll` | Runtime seed/key algorithm dependency for UDS security access. |
| Source archive | `Diagnostics\UDSSystem\SecurityAccess\Sources.zip` | Source package for the security access example. |
| Source tree | `Diagnostics\UDSSystem\SecurityAccess\Sources\...` | Build/source artifacts for the seed/key DLL. Contains DLL outputs and project/source files. Treat as dependency source, not as something to execute during static analysis. |

## Panels and System Variables

| Asset group | Paths | Purpose |
| --- | --- | --- |
| Panels | `Diagnostics\UDSSystem\Panels\DoorFL.xvp`; `DoorFR.xvp`; `ExternalSignals.xvp`; `tester.xvp`; `VariantCoding.xvp`; `Help.xvp` | User interaction panels for ECU state, tester actions, external signals, and variant coding. |
| System variables | `Diagnostics\UDSSystem\SystemVariables\OpenDoorContacts.vsysvar`; `SV_EcuSim.vsysvar`; `SV_ExternalSignals.vsysvar`; `SV_FaultMemory.vsysvar`; `SV_VehicleSim.vsysvar` | System-variable namespaces used by panels and CAPL nodes. |
| Macros | `Diagnostics\UDSSystem\Macros\DoorFL_ReadEcuRelatedInfo.asc`; `DoorFL_SetVariantCodingUSA.cs` | Reusable scripted actions for reading ECU info and setting variant coding. |

## Test Assets

| Asset | Path | Purpose |
| --- | --- | --- |
| XML test module | `Diagnostics\UDSSystem\Testmodules\XML_Tester_ECU1.vxt` | XML-based diagnostic test module. |
| vTESTstudio project | `Diagnostics\UDSSystem\Testunits\vTESTstudio_DiagTest.vtsoproj` | vTESTstudio project for diagnostic testing. |
| vTESTstudio properties | `Diagnostics\UDSSystem\Testunits\vTESTstudio_DiagTest.vvarprop` | vTESTstudio variable/property data. |
| Test unit | `Diagnostics\UDSSystem\Testunits\DiagTest\DiagTest.vtt` | vTESTstudio test unit. |
| Compiled test unit | `Diagnostics\UDSSystem\Testunits\DiagTest\DiagTest.vtuexe` | Compiled test-unit executable artifact. Do not execute during static analysis. |

## Related CAN Diagnostic Assets

| Asset | Path | Purpose |
| --- | --- | --- |
| CANSystem CDD | `CANSystemDemo\CDD\CANSystem.cdd` | Diagnostic description in the full classic CAN system demo. |
| Door CDD | `CANSystemDemo\CDD\CANSystemDoor.cdd` | Door-specific diagnostic description in classic CAN demo. |
| TestFeatureSet UDS CDD | `TestFeatureSet\CentralLockingSystem\DBs\SampleUDS.cdd` | UDS-related CDD for test feature set sample. |
| Seat KWP CDD | `TestFeatureSet\SeatTest\DBs\kwp2000-seat.cdd` | KWP diagnostic CDD. Useful as contrast, not the main UDS path. |

## Handling Rules

- Do not execute DLL, EXE, VTUEXE, BAT, or generated artifacts during static analysis.
- Treat CDD/PDX as diagnostic source-of-truth artifacts, but inspect them through CANoe/diagnostic tooling when detailed service metadata is required.
- Use CAPL files to understand executable behavior, because they show how the sample responds to services, panels, system variables, and test modules.
