import pytest
from typing import Dict, List

from mock_slack_client import MockSlackClient
from slck.user import User, UserManager, UserNotFoundError


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

    def test__cannot_find_user(self) -> None:
        client: MockSlackClient = MockSlackClient()
        user_manager: UserManager = UserManager(client)
        with pytest.raises(UserNotFoundError):
            user_manager.find(real_name="No One")
