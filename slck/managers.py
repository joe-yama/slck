from dataclasses import asdict
from typing import List, Optional, Dict

from slack_sdk import WebClient
from slack_sdk.web import SlackResponse


from slck.channel import Channel
from slck.user import User
from slck.message import Message


class ChannelNotFoundError(Exception):
    pass


class UserNotFoundError(Exception):
    pass


class ChannelManager:
    def __init__(self, client: WebClient) -> None:
        self.client: WebClient = client

    def list(self, prefix: str = "") -> List[Channel]:
        next_cursor: str = ""  # for pagenation
        hit_channels: List[Channel] = []
        while True:
            response: SlackResponse = self.client.conversations_list(
                types="public_channel,private_channel",
                limit=200,
                cursor=next_cursor,
            )
            for channel in response["channels"]:
                channel_name = channel["name_normalized"]
                if channel_name.startswith(prefix):
                    hit_channels.append(Channel(channel["id"], channel_name))
            next_cursor = response["response_metadata"]["next_cursor"]
            if not next_cursor:
                break
        return hit_channels

    def find(self, name: str) -> Dict:
        for channel in self.list(prefix=name):
            if channel.name == name:
                return asdict(channel)
        raise ChannelNotFoundError(f"Channel named {name} is not found.")


class UserManager:
    def __init__(self, client: WebClient) -> None:
        self.client = client

    def list(self) -> List[User]:
        next_cursor: str = ""  # for pagenation
        hit_users: List[User] = []
        while True:
            response: SlackResponse = self.client.users_list(
                limit=200, cursor=next_cursor
            )
            for user in response["members"]:
                if user["is_bot"]:
                    continue
                hit_users.append(
                    User(
                        id=user["id"],
                        name=user["name"],
                        real_name=user.get("real_name", None),
                    )
                )
            next_cursor = response["response_metadata"]["next_cursor"]
            if not next_cursor:
                break
        return hit_users

    def find(
        self,
        id: Optional[str] = None,
        name: Optional[str] = None,
        real_name: Optional[str] = None,
    ) -> Dict:
        for user in self.list():
            if id is None or user.id == id:
                if name is None or user.name == name:
                    if real_name is None or user.real_name == real_name:
                        return asdict(user)
        raise UserNotFoundError


class MessageManager:
    def __init__(self, client: WebClient) -> None:
        self.client = client

    def list(self, channel: str, limit: int = 10) -> None:
        pass
