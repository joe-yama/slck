from dataclasses import dataclass
from typing import Optional

from slck.user import User


@dataclass
class Message:
    user: User
    ts: str
    text: str
    num_reply: int
    num_replyuser: int
    num_reaction: int
