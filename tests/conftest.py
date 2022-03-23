import os

import pytest
import dotenv


@pytest.fixture
def token() -> str:
    dotenv.load_dotenv()
    token: str = os.environ["SLACK_BOT_TOKEN"]
    return token