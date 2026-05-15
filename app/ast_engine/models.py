from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class ConstantRecord:
    file: str
    class_name: Optional[str]
    function_name: Optional[str]
    name: str
    value: Any
    line: int
    scope: str