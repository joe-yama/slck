from typing import Dict, List

import pytest
from mock_slack_client import MockSlackClient
from slck.channel import Channel
from slck.managers import (
    ChannelManager,
    ChannelNotFoundError,
    MessageManager,
    UserManager,
)
from slck.message import Message
from slck.user import User


class TestChannelManager:
    def test__initialize(self) -> None:
        client: MockSlackClient = MockSlackClient()
        channel_manager: ChannelManager = ChannelManager(client)
        assert channel_manager.client.token == "dummy-token"

    def test__list_channels_without_prefix(self) -> None:
        client: MockSlackClient = MockSlackClient()
        channel_manager: ChannelManager = ChannelManager(client)
        channels: List[Channel] = channel_manager.list()
        assert len(channels) == 2

    def test__list_channels_with_prefix(self) -> None:
        client: MockSlackClient = MockSlackClient()
        channel_manager: ChannelManager = ChannelManager(client)
        channels: List[Channel] = channel_manager.list(prefix="gene")
        assert len(channels) == 1
        assert channels[0].name == "general"

    def test__find_general_channel_by_name(self) -> None:
        client: MockSlackClient = MockSlackClient()
        channel_manager: ChannelManager = ChannelManager(client)
        channel: Dict = channel_manager.find(name="general")
        assert channel["name"] == "general"
        assert channel["id"] == "C111"

    def test__find_random_channel_by_name(self) -> None:
        client: MockSlackClient = MockSlackClient()
        channel_manager: ChannelManager = ChannelManager(client)
        channel: Dict = channel_manager.find(name="random")
        assert channel["name"] == "random"
        assert channel["id"] == "C222"

    def test__find_random_channel_by_id(self) -> None:
        client: MockSlackClient = MockSlackClient()
        channel_manager: ChannelManager = ChannelManager(client)
        channel: Dict = channel_manager.find(id="C222")
        assert channel["name"] == "random"
        assert channel["id"] == "C222"

    def test__find_no_channel(self) -> None:
        client: MockSlackClient = MockSlackClient()
        channel_manager: ChannelManager = ChannelManager(client)
        with pytest.raises(ChannelNotFoundError):
            channel_manager.find(name="fake-channel")


class TestUserManager:
    def test__initialize(self) -> None:
        client: MockSlackClient = MockSlackClient()
        UserManager(client)

    def test__list_users(self) -> None:
        # client: WebClient = WebClient(token)
        client: MockSlackClient = MockSlackClient()
        user_manager: UserManager = UserManager(client)
        users: List[User] = user_manager.list()
        assert len(users) == 2

    def test__find_user_by_id(self) -> None:
        client: MockSlackClient = MockSlackClient()
        user_manager: UserManager = UserManager(client)
        user: Dict = user_manager.find(id="W07QCRPA4")
        assert user["id"] == "W07QCRPA4"
        assert user["name"] == "glinda"
        assert user["real_name"] == "Glinda Southgood"

    def test__find_user_by_name(self) -> None:
        client: MockSlackClient = MockSlackClient()
        user_manager: UserManager = UserManager(client)
        user: Dict = user_manager.find(name="glinda")
        assert user["id"] == "W07QCRPA4"
        assert user["name"] == "glinda"
        assert user["real_name"] == "Glinda Southgood"

    def test__find_user_by_real_name(self) -> None:
        client: MockSlackClient = MockSlackClient()
        user_manager: UserManager = UserManager(client)
        user: Dict = user_manager.find(real_name="Glinda Southgood")
        assert user["id"] == "W07QCRPA4"
        assert user["name"] == "glinda"
        assert user["real_name"] == "Glinda Southgood"


class TestMessageManager:
    def test__initialize(self) -> None:
        client: MockSlackClient = MockSlackClient()
        MessageManager(client)

    def test__list(self) -> None:
        client: MockSlackClient = MockSlackClient()
        message_manager: MessageManager = MessageManager(client)
        messages: List[Message] = message_manager.list(channel_id="C111")
        assert len(messages) == 4

    # def test__list_real(self, token):
    #     client: WebClient = WebClient(token)
    #     message_manager: MessageManager = MessageManager(client)
    #     messages: List[Message] = message_manager.list(channel_id="C037SCK8V27")
