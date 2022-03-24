from dataclasses import dataclass
from typing import Dict, List

from slck.user import User


@dataclass
class Message:
    message_type: str
    user: User
    ts: str
    text: str
    num_reply: int
    num_replyuser: int
    num_reaction: int


def parse_message(message: Dict) -> Message:
    message_type: str = message["type"]
    user: User = User(id=message["user"])
    ts: str = message["ts"]
    text: str = message["text"]
    num_reply: int = message.get("reply_count", 0)
    num_replyuser: int = len(message.get("reply_users", []))
    reactions: List = message.get("reactions", [])
    num_reaction = sum([reaction.get("count", 0) for reaction in reactions])
    return Message(
        message_type=message_type,
        user=user,
        ts=ts,
        text=text,
        num_reply=num_reply,
        num_replyuser=num_replyuser,
        num_reaction=num_reaction,
    )
