# 长安 B216-G 角雷达诊断测试系统

基于 Vector CANoe 12.0 的 UDS 诊断测试工程，用于 **长安 B216-G 车型**四路角雷达传感器（左前 FL、右前 FR、左后 RL、右后 RR）的诊断通信、标定与配置。

---

## 1. 功能特性

| 功能 | 说明 |
|------|------|
| **UDS 诊断** | 基于 ISO 14229-1 统一诊断服务，通过 CAN 总线与雷达 ECU 通信 |
| **雷达标定** | 在线/动态标定（RoutineControl 0x31 01 23 01），读取标定状态 (0x22 FD0C) 和安装角度偏差 (0x22 FD1C) |
| **VIN 编程** | 通过 DID 0xF190 写入/读取 17 位 VIN 码，支持 ISO-TP 多帧传输 |
| **车辆配置 (DID5002)** | 通过 DID 0x5002 写入 64 字节车辆配置，区分燃油车/电动车参数 |
| **安全访问** | 0x27 服务 Seed-Key 解锁，使用外部 DLL（`GenerateKeyEx.dll`）生成密钥 |
| **自动化测试** | CAPL Test 模块自动执行测试用例，生成 XML 格式测试报告 |
| **日志记录** | Measurement Setup Logging Block + 手动 CAPL ASC 日志双通道记录 |
| **信号监控** | 统计 CAN 信号值出现次数 |

---

## 2. 目录结构

```
长安_B216-G/
├── 长安_B216-G.cfg          # 主 CANoe 配置文件 (12.0, 32 PRO)
├── 长安_B216-G_260127.cfg   # 备用配置 (日期版本 2026-01-27)
├── GenerateKeyEx.dll         # Seed-Key 生成 DLL (主文件, ~936 KB)
├── DID5002_系统变量配置说明.md # DID5002 配置文档
│
├── code/                     # CAPL 源代码
│   ├── FL_uds.can            # ★ 主诊断脚本 (核心, ~2145行)
│   ├── FL.can                # FL 雷达脚本 (早期版本)
│   ├── FR.can                # FR 雷达脚本
│   ├── LR.can                # LR 雷达脚本
│   ├── RR.can                # RR 雷达脚本
│   ├── FL_Test.can           # 自动化测试脚本
│   ├── FL可同步4R的标定.can    # FL 同步四雷达标定脚本
│   ├── 读取标定.can           # 一键读取四雷达标定数据
│   ├── GetSingalTimes.can    # 信号统计工具
│   ├── GetSingalTimes1.can   # 信号统计工具 (副本)
│   ├── fl_uds_test.can       # FL_uds 测试/调试脚本
│   └── ReportAndLog.cin      # 日志模块包含文件
│
├── panel/                    # CANoe Panel 面板文件
│   └── 面板.xvp               # 主操作面板
│
├── sys/                      # 系统变量定义
│   └── sys_20260428.vsysvar  # 最新系统变量 (2026-04-28)
│
├── CDD/                      # CANdela 诊断描述文件
│   ├── B216-G/               # B216-G 平台专用 CDD (推荐使用)
│   ├── SDA_C928-2_11.0_*.cdd # C928-2 平台通用 CDD
│   ├── 长安4路角雷达CDD.110/  # 角雷达系列备用版本
│   └── 产线/                  # 产线/工厂专用 CDD
│
├── DBC/                      # CAN 数据库文件
│   ├── 0ADASCCAN_*前角雷达*.dbc  # ADASCCAN 前角雷达网络
│   ├── 0ADASBCAN_*后角雷达*.dbc  # ADASBCAN 后角雷达网络
│   ├── PCAN_Fusion_LR_RR_V0.300.dbc  # 后雷达融合网络
│   ├── 1CHSCAN_IBCU 3 - ESP B216.dbc # ESP 制动系统
│   ├── C928-2项目HEV协议*.dbc       # HEV 混动通信
│   └── ABDRobot1126.DBC             # 机器人/自动化接口
│
├── DLL/                      # 各雷达独立 Seed-Key DLL
│   ├── GenerateKeyEx_FL.dll
│   ├── GenerateKeyEx_FR.dll
│   ├── GenerateKeyEx_RL.dll
│   └── GenerateKeyEx_RR.dll
│
├── Log/                      # ASC 诊断日志输出
├── .vscode/                  # VS Code 设置 (GBK 编码, CAPL 语法高亮)
└── .cursor/                  # Cursor 编辑器规则
```

---

## 3. 技术架构

```
┌──────────────────────────────────────────────┐
│  Panel UI (.xvp)                             │
│  按钮控件绑定到系统变量 (Button_*, DiagControl::*)  │
└──────────────────┬───────────────────────────┘
                   │ sysvar_update 回调
┌──────────────────▼───────────────────────────┐
│  CAPL 脚本层 (code/*.can)                     │
│  - FL_uds.can: 主诊断引擎                     │
│  - UDS 请求构建 / ISO-TP 封装 / 响应解析        │
│  - 双雷达串联执行 + ServiceGap 时序控制          │
└──────────────────┬───────────────────────────┘
                   │ diagSendRequest / output
┌──────────────────▼───────────────────────────┐
│  CAN 总线层                                   │
│  CAN1: FL (Tx=0x766/Rx=0x76E), FR (0x767/0x76F)│
│  CAN2: RL (Tx=0x753/Rx=0x75B), RR (0x754/0x75C)│
└──────────────────┬───────────────────────────┘
                   │
┌──────────────────▼───────────────────────────┐
│  DLL 层: GenerateKeyEx.dll                   │
│  Seed-Key 安全算法 (diagGenerateKeyFromSeed)   │
└──────────────────┬───────────────────────────┘
                   │
┌──────────────────▼───────────────────────────┐
│  日志层: Log/*.asc + Logging Block            │
│  CAN 原始流量 ASC 格式记录                      │
└──────────────────────────────────────────────┘
```

### ECU 信息表

| 产品 | 位置 | CAN 通道 | 请求 ID (Tx) | 响应 ID (Rx) |
|------|------|----------|-------------|-------------|
| **B216_FL** | 左前 (Front Left) | CAN1 | 0x766 | 0x76E |
| **B216_FR** | 右前 (Front Right) | CAN1 | 0x767 | 0x76F |
| **B216_RL** | 左后 (Rear Left) | CAN2 | 0x753 | 0x75B |
| **B216_RR** | 右后 (Rear Right) | CAN2 | 0x754 | 0x75C |

---

## 4. CAPL 脚本说明

### 4.1 FL_uds.can — 主诊断脚本（核心）

最完整的诊断脚本，支持全部四个雷达。核心机制：

- **诊断状态机** (`enum DiagStep`)：IDLE → 扩展会话 → 安全访问(Seed→Key) → 标定启动 → 读取标定状态 → 读取安装角度 → VIN 写入/读取 → DID5002 写入/读取
- **ISO-TP 多帧传输**：首帧 (0x10) + 流控帧 (0x30) + 连续帧 (0x21-0x29)，支持 STmin 和 BlockSize 控制
- **双雷达串联执行**：FL(766) 标定完成后自动启动 RR(754) 标定（`gRadarSeqFLThenRR` 机制）
- **ServiceGap 时序**：每个 UDS 服务完成后延迟 20ms (`SERVICE_GAP_MS`) 再触发下一步，避免总线冲突
- **ASC 日志双通道**：Measurement Logging Block (0x700~0x7DF) + 手动 CAPL `openFileWrite` 日志
- **诊断请求类型**：通过 `Radar_Type` 系统变量（1=FL, 2=FR, 3=RL, 4=RR）切换目标雷达

### 4.2 FL.can / FR.can / LR.can / RR.can

早期版各雷达独立脚本，基于 CDD 诊断描述 (`diagRequest` 对象)，功能相对简单：
- 扩展会话 / 安全访问 / 离线动态标定 / 配置写入
- 通过 `on Message` 直接解析 CAN 帧响应（不使用 ISO-TP 封装）
- 板载 Button 按钮控制（1003: 扩展会话, 2301: 动态标定, 5002: 油车/电车配置）

### 4.2.1 FL可同步4R的标定.can

FL 雷达同步四雷达标定脚本，扩展了 `FL.can` 的功能，支持一次操作同步标定四个角雷达。

### 4.2.2 fl_uds_test.can

`FL_uds.can` 的测试/调试版本脚本。

### 4.3 FL_Test.can — 自动化测试脚本

基于 CAPL Test 框架，自动执行测试用例并生成 XML 报告：
- 测试用例：扩展会话、安全访问、启动标定、读取标定状态、读取安装角度
- 输出 XML 格式测试报告（Pass/Fail + 详细信息）

### 4.4 读取标定.can — 一键读取标定数据

简洁版脚本，通过一个按钮（`Button_Read_calibration`）同时读取四个雷达的安装角度偏差值。

### 4.5 GetSingalTimes.can / GetSingalTimes1.can — 信号统计工具

监控 CAN3::LR::LR_RDI_Header::LR_MaxDetectionRange 信号，统计各信号值 (0-4) 在整个测量期间的累计出现次数。两个文件功能相同。

### 4.6 ReportAndLog.cin — 日志包含文件

被 `FL_uds.can` 引用的公共模块，提供：
- `InitUdsLoggingTime()`：获取本地时间戳
- `loggingStart(char title[])`：启动 Logging Block，生成带时间戳的 ASC 文件名
- `loggingStop()`：停止 Logging Block

---

## 5. Panel 面板与系统变量

### 5.1 Button 命名空间（按钮控件）

| 变量名 | 功能 |
|--------|------|
| `Button_FL_1003` ~ `Button_RR_1003` | 扩展诊断会话 (0x10 03) |
| `Button_FL_22FD0C` | FL 读取标定状态 (0x22 FD0C) |
| `Button_FL_22FD1C` | FL 读取安装角度 (0x22 FD1C) |
| `Button_FL_2301` ~ `Button_RR_2301` | 标定启动 (0x31 01 23 01) |
| `Button_FL_5002` ~ `Button_RR_5002` | 写入 DID5002 (油车配置) |
| `Button_FL_5002_HEV` ~ `Button_RR_5002_HEV` | 写入 DID5002 (电车配置) |
| `Button_FL_F190` | FL VIN 写入 (0x2E F190) |
| `Button_Read_calibration` | 一键读取四雷达标定数据 |

### 5.2 DiagControl 命名空间（诊断控制）

| 变量名 | 类型 | 说明 |
|--------|------|------|
| `Btn_Calibration` | int | 触发完整标定流程 |
| `Btn_ReadDTC` | int | 触发 DTC 读取 |
| `DID5002_Byte10` | int | DID5002 字节 10 配置值 |
| `DID5002_Byte44` | int | DID5002 字节 44 配置值 (项目代码) |
| `DID5002_Byte46` | int | DID5002 字节 46 配置值 (硬件变体) |
| `Input_VIN` | string | VIN 输入 (17 位字符) |
| `Radar_Type` | int | 雷达选择 (0=default, 1=FL, 2=FR, 3=RL, 4=RR) |

DID5002 Byte44 值含义：0=Invalid, 4=C857, 6=C518, 8=C798, 9=C390, 20=C928OIL, 27=C857ASE, **39=B216**

---

## 6. UDS 诊断流程

### 6.1 完整标定流程

```
扩展会话 (10 03)
    ↓
安全访问 Seed 请求 (27 01) → ECU 返回 Seed
    ↓
安全访问 Key 发送 (27 02) → DLL 计算 Key
    ↓
启动标定 RoutineControl (31 01 23 01)
    ↓
读取标定状态 ReadDataByIdentifier (22 FD0C)
    ↓
读取安装角度偏差 (22 FD1C)
    ↓ (完整流程自动继续)
VIN 写入 (2E F190) → ISO-TP 多帧传输
    ↓
VIN 读取验证 (22 F190)
    ↓
DID5002 写入 (2E 50 02) → ISO-TP 多帧 (1×FF + 9×CF)
    ↓
DID5002 读取验证 (22 50 02)
```

### 6.2 双雷达串联机制

当选择 FL 雷达执行完整标定流程时，FL(766) 完成 FD1C 读取后，自动启动 RR(754) 的会话建立和状态读取：
- `gRadarSeqFLThenRR`：标志位，1=启用串联模式
- `gRadarSeqOnRRPhase`：1=当前为 RR 阶段，0=FL 阶段
- 独立状态回调同样适用于 RR 雷达 (`gSeqStatFLThenRR`)

### 6.3 ISO-TP 多帧传输

VIN 写入 (18 字节) 和 DID5002 写入 (67 字节) 均需要 ISO-TP 分段传输：

```
首帧 (FF): 1x 43 ...     (4 字节 PDU 信息 + 数据)
流控帧 (FC): 30 00 0X    (ECU 返回, BS + STmin)
连续帧 (CF): 2x ...      (序号 0x21~0x2F + 7 字节数据)
```

FL_uds.can 中通过 `tSTmin_VIN` / `tSTmin_DID5002` 定时器精确控制 CF 发送间隔。

### 6.4 标定状态码

| 状态值 | 含义 |
|--------|------|
| 0x00 | 未标定 |
| 0x01 | 标定中 |
| 0x02 | 标定成功 |
| 0x03 | 标定失败 |

---

## 7. DID5002 配置说明

DID5002 (2E 50 02 / 22 50 02) 为车辆配置标识符，包含 64 字节有效载荷。

详细的 Panel 控件绑定、下拉框选项配置、数据映射关系和测试步骤请参阅专门文档：[DID5002_系统变量配置说明.md](DID5002_系统变量配置说明.md)

### 关键字节映射

```
UDS 请求帧 (67 字节): [2E 50 02] + [64 字节 payload]
                                ├── payload[10] (Byte 13): 车辆配置类型
                                ├── payload[44] (Byte 47): 项目代码
                                └── payload[46] (Byte 49): 硬件变体
```

### 配置区别

| 项目 | Byte 10 燃油车 | Byte 10 电动车 |
|------|---------------|---------------|
| B216 默认 | 0x29 | 0x30 |
| C928 HEV | — | 0x30 |

---

## 8. CDD 与 DBC 文件

### CDD 文件

CDD 文件存在三个版本，使用时请注意选择：

| 版本 | 路径 | 适用场景 |
|------|------|----------|
| **B216-G 专用** | `CDD/B216-G/B216-G_11.0_*.cdd` | ★ B216-G 车型推荐使用 |
| C928-2 平台 | `CDD/SDA_C928-2_11.0_*.cdd` | C928-2 平台通用版本 |
| 产线版本 | `CDD/产线/` | 工厂产线带出厂标定参数 |

### DBC 文件及 CAN 网络

| DBC 文件 | CAN 网络 | 说明 |
|----------|----------|------|
| `0ADASCCAN_*前角雷达*.dbc` | ADASCCAN | 前角雷达 (FL/FR) 信号定义 |
| `0ADASBCAN_*后角雷达*.dbc` | ADASBCAN | 后角雷达 (RL/RR) 信号定义 |
| `PCAN_Fusion_LR_RR_V0.300.dbc` | PCAN_Network | 后雷达融合数据网络 |
| `1CHSCAN_IBCU 3 - ESP B216.dbc` | CHSCAN | ESP/制动系统通信 |
| `C928-2项目HEV协议*-mADC.dbc` | mADC | 混合动力车辆通信 |
| `ABDRobot1126.DBC` | — | 自动化机器人接口 |

---

## 9. DLL 安全访问

### GenerateKeyEx.dll

安全访问 (0x27) 依赖外部 DLL 计算 Key 值：
- **根目录** `GenerateKeyEx.dll`：主 DLL 文件 (~936 KB, PE32)
- **DLL/ 子目录**：各雷达独立副本 (`GenerateKeyEx_FL/FR/RL/RR.dll`)

CAPL 调用接口：
```c
diagGenerateKeyFromSeed("FL", SeedArray, elcount(SeedArray), 1,
                        "", "", KeyArray, elcount(KeyArray), KeyActualSize);
```

工作流程：
1. CAPL 发送 27 01 请求 Seed
2. ECU 返回 67 01 + 4 字节 Seed
3. CAPL 调用 DLL 计算 Key
4. CAPL 发送 27 02 + Key 解锁 ECU

---

## 10. 环境要求

| 环境 | 版本/说明 |
|------|----------|
| **Vector CANoe** | 12.0.221 (32 PRO 版本) |
| **操作系统** | Windows |
| **CAN 硬件** | Vector CAN 卡 (VN16xx 或其他 Vector 接口) |
| **编码** | GBK (936) — 脚本中文注释和 Panel 控件文本 |
| **DLL** | GenerateKeyEx.dll (需与 CANoe 在同一目录或 PATH) |
| **编辑器** | 推荐 VS Code + `.vscode/settings.json` 中配置的 CAPL 语法高亮 |

---

## 11. 快速上手

### 11.1 打开工程

1. 双击 `长安_B216-G.cfg` 启动 CANoe 12.0
2. CANoe 自动加载 DBC 文件和 CAPL 脚本节点
3. 加载 B216-G 专用 CDD 文件：`CDD/B216-G/B216-G_11.0_*.cdd`
4. 打开 Panel 面板：`panel/面板.xvp`

### 11.2 基本操作流程

1. **选择雷达**：Panel 上 `Radar_Type` 下拉框选择目标雷达 (B216_FL/B216_FR/B216_RL/B216_RR)
2. **进入扩展会话**：点击对应雷达的 `10 03` 按钮
3. **执行标定**：点击 `Btn_Calibration` 触发完整标定流程（或点击 `2301` 仅标定）
4. **读取标定状态**：点击 `22FD0C` 查看标定结果
5. **写入 VIN**：在 `Input_VIN` 输入 17 位 VIN，点击 `F190` 写入
6. **配置车辆类型**：选择 DID5002 各字节值，点击 `5002` (燃油) 或 `5002_HEV` (电动) 写入
7. **一键读取标定**：点击 `Read_calibration` 同时读取四个雷达

### 11.3 查看日志

- ASC 日志自动保存在 `Log/` 目录，文件命名格式：`UDS_YYYY_MM_DD_HH_MM_SS_<测试描述>.asc`
- CANoe Trace 窗口可实时查看 CAN 帧交互
- Write 窗口输出 CAPL `write()` 调试信息

### 11.4 运行自动化测试

1. 在 CANoe Measurement Setup 中添加 `FL_Test.can` 为 Test Node
2. 启动 Measurement
3. 测试自动运行，生成 XML 格式报告

---

## 12. 参考文档

- [DID5002 系统变量配置说明](DID5002_系统变量配置说明.md) — Panel 控件配置与测试步骤
- CANdela CDD 文件：`CDD/B216-G/B216-G_11.0_*.cdd`
- DBC 数据库：`DBC/` 目录下各网络数据库文件
- CANoe 工程配置：`长安_B216-G.cfg`
