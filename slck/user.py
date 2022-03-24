from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    id: str
    name: str
    real_name: Optional[str] = None
