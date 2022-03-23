from typing import List

from slack_sdk import WebClient

from slck.channel import Channel
from slck.user import User
from slck.message import Message


class ChannelManager(WebClient):
    def list(self) -> None:
        pass

    def find(self, name: str) -> Channel:
        return Channel(id="channelid", name="channelname")


class UserManager(WebClient):
    def list(self) -> List[User]:
        return [User(id="myid", name="myname", real_name="myreak¥lname")]

    def find(self, name: str, from_realname: bool = True) -> User:
        return User(id="myid", name="myname", real_name="myreak¥lname")


class MessageManager(WebClient):
    def list(self, channel: str, limit: int = 10) -> None:
        pass
