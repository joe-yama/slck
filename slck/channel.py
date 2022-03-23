from dataclasses import dataclass


@dataclass
class Channel:
    id: str
    name: str

    def __str__(self) -> str:
        return self.name