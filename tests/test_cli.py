from slck.cli import SlackManager
from slck.channel import Channel


class TestSlackManager:
    def test__initialize(self, token: str) -> None:
        SlackManager(token)

    def test__channel_list(self, token: str) -> None:
        slack: SlackManager = SlackManager(token)
        slack.channel.list()

    def test__channel_find(self, token: str) -> None:
        slack: SlackManager = SlackManager(token)
        c: Channel = slack.channel.find(name="channelid")
        assert c.id == "channelid"