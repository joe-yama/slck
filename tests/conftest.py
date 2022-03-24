import os
from typing import Optional

import dotenv
import pytest


@pytest.fixture
def token() -> str:
    dotenv.load_dotenv(override=True)
    token: Optional[str] = os.getenv("SLACK_BOT_TOKEN")
    if token is None:
        raise KeyError("SLACK_BOT_TOKEN is not found.")
    return token
