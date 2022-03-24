from dataclasses import dataclass
from typing import Dict, List

from slack_sdk import WebClient
from slack_sdk.web import SlackResponse
from slck.channel import ChannelManager
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


class MessageManager:
    def __init__(self, client: WebClient) -> None:
        self.client = client

    def list(
        self,
        channel: str,  # channel id or channel name (depends on argument `name`)
        name: bool = True,  # if False, `channel` is considered as channel ID
    ) -> List[Message]:
        channel_id: str = ""
        if name:
            channel_manager: ChannelManager = ChannelManager(self.client)
            channel_id = channel_manager.find(name=channel)["id"]
        else:
            channel_id = channel

        messages: List[Message] = []
        next_cursor: str = ""  # for pagenation
        while True:
            response: SlackResponse = self.client.conversations_history(
                channel=channel_id, next_cursor=next_cursor
            )
            for message in response["messages"]:
                if message["type"] == "message":
                    m = parse_message(message)
                    messages.append(m)
            if response["has_more"] is True:
                next_cursor = response["response_metadata"]["next_cursor"]
            else:
                break
        return messages
