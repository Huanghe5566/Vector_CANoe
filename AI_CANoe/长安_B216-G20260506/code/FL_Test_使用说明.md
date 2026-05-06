# FL雷达诊断测试 - CAPL Test 模块使用说明

## 文件说明

| 文件名 | 说明 |
|--------|------|
| `FL_Test.can` | CAPL Test测试脚本（主文件） |
| `FL_Test.cbf` | 测试模块配置文件（自动生成） |

## 功能特性

1. **标准化测试框架** - 基于CAPL Test标准测试用例结构
2. **XML报告输出** - 生成标准XML格式测试报告
3. **详细测试步骤** - 每个诊断服务单独测试用例
4. **负响应处理** - 自动检测NRC并记录错误
5. **PASS/FAIL判定** - 自动判断测试结果

## 测试用例列表

| 测试用例 | 服务 | 描述 |
|----------|------|------|
| tc_InitFLTest | - | 测试初始化，设置报告路径 |
| tc_ExtendedSession | 0x10 03 | 进入扩展诊断会话 |
| tc_SecurityAccess | 0x27 | Seed-Key安全访问解锁 |
| tc_StartCalibration | 0x31 01 23 01 | 启动标定例程 |
| tc_ReadCalibrationStatus | 0x22 FD0C | 读取标定状态 |
| tc_ReadAngleDeviation | 0x22 FD1C | 读取安装角度偏差 |

## XML报告格式

生成的XML报告结构如下：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<TestReport>
  <Header>
    <Title>FL雷达诊断测试报告</Title>
    <StartTime>2025-01-27 14:30:00</StartTime>
    <TestObject>前左(FL)雷达</TestObject>
    <CAN_ID>Request: 0x766, Response: 0x76E</CAN_ID>
  </Header>
  <TestCases>
    <TestCase name="ExtendedSession">
      <Description>进入扩展会话(0x10 03)</Description>
      <Result>PASS</Result>
      <Details>请求ID: 0x766, 服务: 10 03</Details>
      <Timestamp>2025-01-27 14:30:05</Timestamp>
    </TestCase>
    <!-- 更多测试用例... -->
  </TestCases>
  <Summary>
    <OverallResult>PASS</OverallResult>
    <SummaryText>所有测试步骤通过</SummaryText>
    <EndTime>2025-01-27 14:30:30</EndTime>
  </Summary>
</TestReport>
```

## 使用方法

### 方法1：在Test Module中运行

1. 在CANoe中创建 **Test Module**（测试模块）
2. 将 `FL_Test.can` 添加到Test Module
3. 在Test Module中调用 `tc_StartTest()` 或 `tc_MainFLTest()`
4. 运行测试，XML报告将自动生成到指定路径

### 方法2：通过Test Tree运行

1. 在CANoe的 **Test Setup** 中导入测试模块
2. 创建测试树，添加各个测试用例
3. 运行测试树，自动生成XML报告

### 方法3：通过CAPL程序调用

```capl
// 在其他CAPL脚本中调用
on key 't' {
  // 启动测试
  tc_StartTest();
}
```

## 报告文件位置

报告默认保存到：
```
F:\AI_Cursor\AI_CANoe\长安_B216-G\test_reports\
```

文件名格式：
```
FL_Radar_Test_YYYYMMDD_HHMMSS.xml
```

## NRC错误码支持

以下NRC码会被自动识别并记录：

| NRC | 描述 |
|-----|------|
| 0x10 | 一般拒绝 |
| 0x11 | 服务不支持 |
| 0x12 | 子功能不支持 |
| 0x13 | 报文长度错误 |
| 0x21 | 忙碌 |
| 0x22 | 条件不支持 |
| 0x31 | 请求超出范围 |
| 0x33 | 安全访问锁定 |
| 0x78 | 响应等待 |

## 注意事项

1. **编码设置**：文件使用GBK编码（936），确保中文正常显示
2. **测试超时**：每个测试步骤默认超时2秒
3. **依赖项**：需要Vector的diagnostic库支持
4. **报告查看**：生成的XML可用浏览器或Excel打开

## 与FL_uds.can的关系

| 文件 | 用途 | 场景 |
|------|------|------|
| `FL_uds.can` | 快速诊断面板操作 | 人工操作、调试 |
| `FL_Test.can` | 自动化测试+报告 | 自动化测试、生产验证 |

两个文件可以独立使用，也可以配合使用。

## 扩展建议

如需添加更多测试用例：

1. 复制现有的testcase模板
2. 修改服务ID和数据
3. 在tc_MainFLTest()中添加调用
4. 更新报告写入逻辑

示例：
```capl
testcase tc_NewTest() {
  TestCaseTitle("新测试项");
  TestCaseDescription("描述...");
  
  // 发送请求
  // 等待响应
  // 判定结果
  
  WriteTestReport("NewTest", "描述", result, details);
}
```
