from typing import List

from slack_sdk import WebClient
from slack_sdk.web import SlackResponse


from slck.channel import Channel
from slck.user import User
from slck.message import Message


class ChannelNotFoundError(Exception):
    pass


class ChannelManager(WebClient):
    def list(self, prefix: str = "") -> List[Channel]:
        next_cursor: str = ""  # for pagenation
        hit_channels: List[Channel] = []
        while True:
            response: SlackResponse = self.conversations_list(
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

    def find(self, name: str) -> Channel:
        for channel in self.list(prefix=name):
            if channel.name == name:
                return channel
        raise ChannelNotFoundError(f"Channel named {name} is not found.")


class UserManager(WebClient):
    def list(self) -> List[User]:
        return [User(id="myid", name="myname", real_name="myreak¥lname")]

    def find(self, name: str, from_realname: bool = True) -> User:
        return User(id="myid", name="myname", real_name="myreak¥lname")


class MessageManager(WebClient):
    def list(self, channel: str, limit: int = 10) -> None:
        pass
