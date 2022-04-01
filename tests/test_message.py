from typing import List, Optional

from mock_slack_client import MockSlackClient
from slck.message import Message, MessageManager


class TestMessageManager:
    def test__initialize(self) -> None:
        client: MockSlackClient = MockSlackClient()
        MessageManager(client)

    def test__list_message_by_channel_id(self) -> None:
        client: MockSlackClient = MockSlackClient()
        message_manager: MessageManager = MessageManager(client)
        messages: List[Message] = message_manager.list(channel="C111", name=False)
        assert len(messages) == 4

    def test__list_message_by_channel_name(self) -> None:
        client: MockSlackClient = MockSlackClient()
        message_manager: MessageManager = MessageManager(client)
        messages: List[Message] = message_manager.list(channel="general", name=True)
        assert len(messages) == 4

    def test__popular_message(self) -> None:
        client: MockSlackClient = MockSlackClient()
        message_manager: MessageManager = MessageManager(client)
        popular_post: Message = message_manager.popular(
            channel="general", name=True, k=1, permalink=True
        )[0]
        assert popular_post.user.id == "W012A3CDE"
        assert popular_post.ts == "1622007986.001500"
        assert popular_post.num_reaction == 3

    def test__award_without_post(self) -> None:
        client: MockSlackClient = MockSlackClient()
        message_manager: MessageManager = MessageManager(client)
        result: str = message_manager.award(channel="general", post=False)
        expected: str = """最もリアクションを獲得したのは@spenglerさんのこのポスト！
https://ghostbusters.slack.com/archives/C1H9RESGA/p135854651500008"""
        assert result is not None
        assert result == expected
