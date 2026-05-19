from __future__ import annotations

# 这个文件负责保存测试证据。
# 当前先保存 JSON，后续可以扩展保存 BLF 路径、PCAP 路径、截图路径、诊断日志等。

import json
from dataclasses import asdict, is_dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


class EvidenceCollector:
    def __init__(self, output_dir: str | Path):
        # mkdir(parents=True, exist_ok=True) 表示：
        # 如果目录不存在就创建；如果已经存在也不报错。
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def write_json(self, name: str, payload: dict[str, Any]) -> Path:
        # 给文件名加时间戳，避免多次运行时互相覆盖。
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = self.output_dir / f"{timestamp}_{name}.json"
        path.write_text(json.dumps(self._to_jsonable(payload), indent=2), encoding="utf-8")
        return path

    def _to_jsonable(self, value: Any) -> Any:
        # dataclass 不能直接 json.dumps，所以先转成普通 dict/list。
        if is_dataclass(value):
            return self._to_jsonable(asdict(value))
        if isinstance(value, dict):
            return {key: self._to_jsonable(item) for key, item in value.items()}
        if isinstance(value, list):
            return [self._to_jsonable(item) for item in value]
        return value
