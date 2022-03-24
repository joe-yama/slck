import os

import dotenv
import pytest
from mock_slack_client import MockSlackClient


@pytest.fixture
def token() -> str:
    dotenv.load_dotenv()
    token: str = os.environ["SLACK_BOT_TOKEN"]
    return token


@pytest.fixture
def mock_client() -> MockSlackClient:
    return MockSlackClient()
