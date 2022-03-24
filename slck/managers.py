from dataclasses import asdict
from typing import Dict, List, Optional

from slack_sdk import WebClient
from slack_sdk.web import SlackResponse
from slck.channel import Channel
from slck.message import Message, parse_message
from slck.user import User


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

    def find(
        self,
        name: Optional[str] = None,
        id: Optional[str] = None,
    ) -> Dict:
        prefix = "" if name is None else name
        for channel in self.list(prefix=prefix):
            if id is None or channel.id == id:
                if name is None or channel.name == name:
                    return asdict(channel)
        raise ChannelNotFoundError


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

    def list(
        self,
        channel_name: str = "",
        channel_id: str = "",
    ) -> List[Message]:
        if channel_id == "" and channel_name == "":
            raise ValueError(
                "One of arguments (channel_id or channel_name) is required."
            )
        if channel_id and channel_name:
            raise ValueError(
                """
                Recieved both of channel_id and channel_name.
                Desired: Either one of arguments (channel_id or channel_name).
            """
            )
        if channel_name:
            channel_manager: ChannelManager = ChannelManager(self.client)
            channel_id = channel_manager.find(name=channel_name)["id"]

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
