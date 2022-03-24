import pytest
from typing import Dict
from typing import List

from mock_slack_client import MockSlackClient
from slck.channel import Channel
from slck.channel import ChannelManager
from slck.channel import ChannelNotFoundError


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