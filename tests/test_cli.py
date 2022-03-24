from slck.cli import SlackManager
from slck.channel import Channel

from mock_slack_client import MockSlackClient


class TestSlackManager:
    def test__initialize(self, token: str) -> None:
        client: MockSlackClient = MockSlackClient()
        SlackManager(client)

    def test__channel_list(self, token: str) -> None:
        client: MockSlackClient = MockSlackClient()
        slack: SlackManager = SlackManager(client)
        slack.channel.list()

    def test__channel_find(self, token: str) -> None:
        client: MockSlackClient = MockSlackClient()
        slack: SlackManager = SlackManager(client)
