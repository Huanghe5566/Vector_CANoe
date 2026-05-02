# CAN / CAN FD / UDS Diagnostics Focused Analysis

This document analyzes the CAN related sample configurations under:

`F:\AI_Codex\CANoe\Sample Configurations 12.0.77\CAN`

The focus is ordinary CAN communication, CAN FD behavior, and UDS diagnostics over CAN. The original CANoe project files were only read and were not modified.

## 1. Recommended Reading Path

1. Start with `Easy\Easy.cfg`.
   - Purpose: understand the smallest CAN signal flow.
   - Key files: `Easy\CANdb\easy.dbc`, `Easy\Nodes\engine.can`, `Easy\Nodes\display.can`, `Easy\Nodes\light.can`.
   - What to learn: CAN database nodes, cyclic/application messages, and simple CAPL node behavior.

2. Move to `CANSystemDemo\CANSystemDemo.cfg`.
   - Purpose: understand a fuller classic CAN vehicle model before CAN FD and diagnostics.
   - Key files: `CANSystemDemo\CANdb\PowerTrain.dbc`, `CANSystemDemo\CANdb\Comfort.dbc`, `CANSystemDemo\Nodes\Gateway.can`, `CANSystemDemo\TestSetup.tse`.
   - What to learn: multiple CAN networks, gateway routing, transport protocol related DBC objects, CDD files, and automated test setup.

3. Study `CAN_FD\CAN_FD_Powertrain.cfg`.
   - Purpose: understand CAN FD database layout, CAN FD to classic CAN routing, DLC checks, and CAN FD test automation.
   - Key files: `CAN_FD\CANdb\CAN_FD_Powertrain.dbc`, `CAN_FD\CANdb\Comfort.dbc`, `CAN_FD\Nodes\CAN_FD_CAN_Gateway.can`, `CAN_FD\Nodes\TFS_CAPL_CAN_FD.can`.
   - What to learn: CAN FD payload width, DLC handling, signal routing between CAN FD and classic CAN, and test feature set checks.

4. Study `Diagnostics\UDSBasic\UDSBasic.cfg`.
   - Purpose: understand the smallest UDS tester and simulated ECU model.
   - Key files: `Diagnostics\UDSBasic\Cdd\UDS-ExampleEcu-5.0.2.cdd`, `Diagnostics\UDSBasic\Nodes\SimDiagECU.can`, `Diagnostics\UDSBasic\Tester\Tester.can`, `Diagnostics\UDSBasic\Tester\TestModule.can`.
   - What to learn: `diagRequest`, `diagResponse`, parameter read/write, raw data handling, positive response, and negative response.

5. Finish with `Diagnostics\UDSSystem\UDSSystem.cfg`.
   - Purpose: understand a complete UDS system with multiple ECUs, panels, system variables, DIDs, security access, downloads, fault memory, macros, and vTESTstudio assets.
   - Key files: `Diagnostics\UDSSystem\Nodes\DoorFL.can`, `Diagnostics\UDSSystem\Nodes\DoorFR.can`, `Diagnostics\UDSSystem\CAPL_Includes\*.cin`, `Diagnostics\UDSSystem\SecurityAccess\SeednKey.dll`, `Diagnostics\UDSSystem\Testunits\vTESTstudio_DiagTest.vtsoproj`.

## 2. Classic CAN Baseline

`Easy` is the cleanest entry point. Its DBC defines nodes `Engine`, `Display`, and `Light`, with a small set of messages such as `EngineState` and `LightState`. This makes it suitable for learning how CANoe maps DBC-defined nodes and signals to CAPL nodes.

`CANSystemDemo` is the better baseline for understanding realistic topology. Its `PowerTrain.dbc` includes nodes such as `Engine` and `Gateway`, diagnostic request/response objects, network management messages, engine data/status messages, gearbox information, and ABS data. Its `Comfort.dbc` adds comfort network nodes, door messages, console messages, gateway messages, and transport-protocol payload messages.

Use these two projects to establish the classic CAN model before comparing CAN FD behavior. The important difference is not only larger payloads: the CAN FD sample also demonstrates explicit test control of DLC and validation of DLC consistency.

## 3. CAN FD Sample

Main entry:

`CAN_FD\CAN_FD_Powertrain.cfg`

Important assets:

- `CAN_FD\CANdb\CAN_FD_Powertrain.dbc`
- `CAN_FD\CANdb\Comfort.dbc`
- `CAN_FD\Nodes\CAN_FD_CAN_Gateway.can`
- `CAN_FD\Nodes\TFS_CAPL_CAN_FD.can`
- `CAN_FD\Vector XML Testmodul CAN FD.vxt`
- `CAN_FD\Teststudio\CAN_FD_Test.vtsoproj`

### 3.1 DBC Model

`CAN_FD_Powertrain.dbc` defines the CAN FD side. It includes nodes `Engine` and `Gateway`. Notable messages include:

- `EngineData`: the main powertrain data frame. The CAPL tests treat it as a CAN FD message and validate DLC behavior.
- `EngineStatus`, `Ignition_Info`, `GearBoxInfo`, and `ABSdata`: vehicle state and powertrain context.
- `Test_Message_CAN_FD`: used to validate large signal payload coverage across many data bytes.
- Diagnostic request/response messages and network-management messages.

`Comfort.dbc` defines the classic CAN comfort side. It includes nodes such as gateway and door/console participants. Notable messages include `Gateway_1`, `Gateway_2`, `DOOR_l`, `DOOR_r`, console messages, TP payload messages, and diagnostic request/response frames.

### 3.2 Gateway Behavior

`CAN_FD\Nodes\CAN_FD_CAN_Gateway.can` is compact and important:

- `on message EngineData`: routes CAN FD frame data to classic CAN signal values in `Comfort::Gateway::Gateway_2`, including engine speed and engine temperature.
- `on message Gateway_2`: routes classic CAN frame data back to the CAN FD powertrain side by assigning `Powertrain::Engine::ABSdata::CarSpeed`.
- `on signal Comfort::Gateway::Gateway_1::Gear`: performs signal-based routing from classic CAN to CAN FD, updating `GearBoxInfo::Gear` and `EngineData::Gear`.

This file is the best place to study frame-based vs signal-based gateway mapping between CAN FD and classic CAN networks.

### 3.3 CAN FD Test Logic

`CAN_FD\Nodes\TFS_CAPL_CAN_FD.can` is the main automation reference. Its `MainTest()` runs:

- `TC1_1_WaitForEngineData`
- `TC1_2_WaitForEngineStatus`
- `TC1_3_WaitForIgnitionInfo`
- `TC2_1_1_CheckInvalidDLC`
- `TC2_1_2_CheckInvalidDLCByNodeTx`
- `TC2_1_3_CheckInvalidDLCByNodeTx`
- `TC3_ChangeSignalValues`
- `TC4_SetMsgDLC`
- `TC5_CheckCycleTime`

The most useful mechanisms are:

- `testWaitForMessage`, `TestGetWaitEventMsgData`, and `testJoinMessageEvent` for message observation.
- `ChkStart_InconsistentDLC`, `ChkStart_InconsistentTxDLC`, and `ChkStart_InconsistentRxDLC` for DLC consistency validation.
- `testSetMsgDlc` and `testResetMsgDlc` for manipulating expected DLC behavior.
- `ChkStart_MsgRelCycleTimeViolation`, `ChkStart_MsgAbsCycleTimeViolation`, and `ChkStart_SignalCycleTimeViolation` for cycle-time checks.

## 4. UDSBasic

Main entry:

`Diagnostics\UDSBasic\UDSBasic.cfg`

Important assets:

- `Diagnostics\UDSBasic\Cdd\UDS-ExampleEcu-5.0.2.cdd`
- `Diagnostics\UDSBasic\Nodes\SimDiagECU.can`
- `Diagnostics\UDSBasic\Tester\Tester.can`
- `Diagnostics\UDSBasic\Tester\TestModule.can`

### 4.1 Simulated ECU

`SimDiagECU.can` implements a simple diagnostic ECU. It stores ECU-like state in CAPL variables:

- `gVehicleSpeedToLockDoor`
- `gEcuIdentification`
- `gVehicleType`

It handles these diagnostic requests:

- `Door.Variant_Coding_Write`: reads physical and symbolic parameters from the request and writes them to simulated ECU memory. It sends NRC `0x31` when the values are outside the expected range.
- `Door.EcuIdentification_Write`: reads a raw 13-byte part number with `GetParameterRaw`.
- `Door.Variant_Coding_Read`: sets response parameters using numerical and physical access modes.
- `Door.EcuIdentification_Read`: sets a raw response parameter with `SetParameterRaw`.
- `Door.SeedLevel_0x01_Request`: intentionally sends a negative response `0x22`.

This is the best minimal example for the ECU side of UDS parameter access.

### 4.2 Tester

`Tester.can` is the matching diagnostic tester. It maps keyboard input to UDS requests:

- Key `1`: writes variant coding using physical and symbolic parameter representations.
- Key `2`: writes a raw part number.
- Key `3`: reads variant coding in symbolic, numerical, physical, and coded representations.
- Key `4`: reads the raw ECU identification value.
- Key `5`: sends a seed request that intentionally receives a negative response.

The tester uses:

- `DiagRequest <service> req`
- `req.SetParameter`
- `req.SetParameterRaw`
- `req.SendRequest`
- `on diagResponse <service>`
- `this.IsPositiveResponse`
- `this.GetResponseCode`
- `this.GetParameter`
- `this.GetParameterRaw`

This file is the best minimal reference for tester-side UDS scripting in CAPL.

## 5. UDSSystem

Main entry:

`Diagnostics\UDSSystem\UDSSystem.cfg`

Important assets:

- `Diagnostics\UDSSystem\CDD\UDS-ExampleEcu-5.0.3.cdd`
- `Diagnostics\UDSSystem\PDX\UDS-ExampleEcu-5.0.2.pdx`
- `Diagnostics\UDSSystem\Nodes\DoorFL.can`
- `Diagnostics\UDSSystem\Nodes\DoorFR.can`
- `Diagnostics\UDSSystem\Nodes\TesterPanelControl.can`
- `Diagnostics\UDSSystem\CAPL_Includes\DiagDefinitions.cin`
- `Diagnostics\UDSSystem\CAPL_Includes\Download_Sim.cin`
- `Diagnostics\UDSSystem\CAPL_Includes\Download_Tester.cin`
- `Diagnostics\UDSSystem\CAPL_Includes\FaultMemory_Sim.cin`
- `Diagnostics\UDSSystem\CAPL_Includes\LibFunctions_Tester.cin`
- `Diagnostics\UDSSystem\SecurityAccess\SeednKey.dll`
- `Diagnostics\UDSSystem\Testmodules\CAPL_Testcases_ECU1.can`
- `Diagnostics\UDSSystem\Testunits\vTESTstudio_DiagTest.vtsoproj`

### 5.1 DoorFL ECU

`DoorFL.can` is the main full-featured ECU simulation. It includes:

- `DiagDefinitions.cin` for shared NRC constants, access modes, fault-memory type, periodic DID mode, and timeout constants.
- `FaultMemory_Sim.cin` for DTC/fault memory simulation.
- `Download_Sim.cin` for download simulation.

Its request handlers cover:

- Generic catch-all handling: `on diagRequest DoorFL.*`
- Tester present
- Diagnostic sessions
- Security access seed/key for multiple levels
- Development data
- Serial number read/write
- Variant coding read/write
- ECU identification read/write
- Voltage and odometer DIDs
- Fingerprint writing
- Window lift rough/fine position read/write
- Multiplexed DID test data read/write
- Periodic data transmission
- Dynamic DID definition/read/clear
- Door status read and IO control
- Communication control
- ECU reset

It also reacts to system variables for fault-memory GUI actions, supply voltage, download progress, and variant coding changes.

### 5.2 DoorFR ECU

`DoorFR.can` is a smaller ECU simulation. It includes shared diagnostic definitions and fault-memory simulation, then implements:

- Tester present
- Sessions
- Development data
- Serial number read
- ECU identification read
- ECU reset

Use it as a comparison point for understanding how much of `DoorFL.can` is optional advanced behavior.

### 5.3 Shared Diagnostic Includes

`DiagDefinitions.cin` defines common UDS negative response codes:

- `0x10` general reject
- `0x11` service not supported
- `0x12` subfunction not supported
- `0x13` incorrect message length or invalid format
- `0x21` busy repeat request
- `0x22` conditions not correct or request sequence error
- `0x24` request sequence error
- `0x31` request out of range
- `0x33` security access denied
- `0x35` invalid key
- `0x78` response pending

It also defines parameter access modes, fault-memory type enum values, periodic DID send modes, and a general application timeout.

`FaultMemory_Sim.cin` is responsible for the DTC/fault memory model. `Download_Sim.cin` and `Download_Tester.cin` split download logic between ECU simulation and tester-side helper behavior. `LibFunctions_Tester.cin` contains reusable tester helper functions.

### 5.4 Security Access

The security access assets are located under:

`Diagnostics\UDSSystem\SecurityAccess`

The key file is `SeednKey.dll`. Source and build artifacts are also present under `SecurityAccess\Sources`, including multiple DLL outputs and source/build files. Treat these as dependency assets: do not execute or modify them unless the goal is specifically to rebuild the Seed/Key algorithm.

### 5.5 Panels, System Variables, Macros, and Test Units

Panels:

- `Panels\DoorFL.xvp`
- `Panels\DoorFR.xvp`
- `Panels\ExternalSignals.xvp`
- `Panels\tester.xvp`
- `Panels\VariantCoding.xvp`
- `Panels\Help.xvp`

System variables:

- `SystemVariables\OpenDoorContacts.vsysvar`
- `SystemVariables\SV_EcuSim.vsysvar`
- `SystemVariables\SV_ExternalSignals.vsysvar`
- `SystemVariables\SV_FaultMemory.vsysvar`
- `SystemVariables\SV_VehicleSim.vsysvar`

Macros:

- `Macros\DoorFL_ReadEcuRelatedInfo.asc`
- `Macros\DoorFL_SetVariantCodingUSA.cs`

Automated testing:

- `Testmodules\CAPL_Testcases_ECU1.can`
- `Testmodules\XML_Tester_ECU1.vxt`
- `Testunits\DiagTest\DiagTest.vtt`
- `Testunits\DiagTest\DiagTest.vtuexe`
- `Testunits\vTESTstudio_DiagTest.vtsoproj`

## 6. Automation View

For CAN FD automation, start with `TFS_CAPL_CAN_FD.can`. It is short and clearly maps test cases to DLC, signal, message, and cycle-time checks.

For UDS automation, start with `UDSBasic\Tester\TestModule.can` to see a smaller diagnostic test module, then move to `UDSSystem\Testmodules\CAPL_Testcases_ECU1.can` and the vTESTstudio project. The UDSSystem test assets are more comprehensive and depend on the full ECU simulation, CDD/PDX diagnostic descriptions, and system variables.

## 7. Practical Reuse Notes

- For learning CAPL diagnostics, copy the patterns from `UDSBasic` first. It has the least indirection.
- For a realistic ECU simulation, use `DoorFL.can` as a feature map, but do not copy it wholesale. Extract one behavior at a time, such as session handling, security access, DID read/write, or fault memory.
- For CAN FD validation, reuse the `TFS_CAPL_CAN_FD.can` structure: message wait checks, DLC checks, signal checks, and cycle-time checks are cleanly separated.
- For gateway behavior, `CAN_FD_CAN_Gateway.can` is the highest-value minimal example because it demonstrates both frame-based and signal-based routing.

## 8. Files Created by This Analysis

- `CAN_CANFD_UDS_Analysis.md`: this report.
- `CAN_CANFD_UDS_Project_Entrypoints.md`: project entrypoint index.
- `CAN_CANFD_UDS_CAPL_Index.md`: CAPL behavior index.
- `CAN_CANFD_UDS_Diagnostic_Assets.md`: diagnostic asset index.
