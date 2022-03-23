from slck.managers import ChannelManager
from slck.managers import UserManager
from slck.managers import MessageManager


class TestChannelManager:
    def test__can_initialize(self, token: str) -> None:
        ChannelManager(token)


class TestUserManager:
    def test__can_initialize(self, token: str) -> None:
        UserManager(token)


class TestMessageManager:
    def test__can_initialize(self, token: str) -> None:
        MessageManager(token)