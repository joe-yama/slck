import os

import dotenv
import fire

from slck.managers import ChannelManager
from slck.managers import UserManager


class SlackManager:
    def __init__(self, token: str) -> None:
        self.__token = token
        self.channel = ChannelManager(self.__token)
        self.user = UserManager(self.__token)


def get_token() -> str:
    dotenv.load_dotenv()
    token: str = os.environ["SLACK_BOT_TOKEN"]
    return token


def main() -> None:
    token: str = get_token()
    slack: SlackManager = SlackManager(token)
    fire.Fire(slack)
