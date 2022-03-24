import json
import os
from typing import Dict, Any

from slack_sdk import WebClient
from slack_sdk.web import SlackResponse

TEST_ROOT_DIR = os.path.dirname(__file__)
TEST_DATA_DIR = os.path.join(TEST_ROOT_DIR, "data")


def get_slackresponse(data: Dict) -> SlackResponse:
    return SlackResponse(
        client=WebClient("dummy"),
        http_verb="GET",
        api_url="http://localhost:8000",
        req_args=dict(),
        data=data,
        headers=dict(),
        status_code=200,
    )


class MockSlackClient(WebClient):
    def __init__(self) -> None:
        super().__init__(token="dummy-token")

    def conversations_list(self, *args: Any, **kwrags: Any) -> SlackResponse:
        with open(
            os.path.join(TEST_DATA_DIR, "web_response_conversions_list.json")
        ) as f:
            web_response: Dict = json.load(f)
            return get_slackresponse(web_response)

    def conversations_join(self, *args: Any, **kwrags: Any) -> SlackResponse:
        pass

    def users_list(self, *args: Any, **kwrags: Any) -> SlackResponse:
        with open(os.path.join(TEST_DATA_DIR, "web_response_users_list.json")) as f:
            web_response: Dict = json.load(f)
            return get_slackresponse(web_response)
