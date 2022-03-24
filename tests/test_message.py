from typing import List

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

    # def test__list_real(self, token):
    #     client: WebClient = WebClient(token)
    #     message_manager: MessageManager = MessageManager(client)
    #     messages: List[Message] = message_manager.list(channel_id="C037SCK8V27")
