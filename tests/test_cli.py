from mock_slack_client import MockSlackClient
from slck.cli import SlackManager


class TestSlackManager:
    def test__initialize(self) -> None:
        client: MockSlackClient = MockSlackClient()
        SlackManager(client)

    def test__channel_list(self) -> None:
        client: MockSlackClient = MockSlackClient()
        slack: SlackManager = SlackManager(client)
        slack.channel.list()

    def test__channel_find(self) -> None:
        client: MockSlackClient = MockSlackClient()
        SlackManager(client)
