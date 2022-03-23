from dataclasses import dataclass


@dataclass
class User:
    id: str
    name: str
    real_name: str

    def __str__(self) -> str:
        return self.real_name
