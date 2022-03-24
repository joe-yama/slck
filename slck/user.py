from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    id: str
    name: Optional[str] = None
    real_name: Optional[str] = None
