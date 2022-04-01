import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

from slack_sdk import WebClient
from slack_sdk.web import SlackResponse

PROJECT_ROOT_DIR: str = str(Path(__file__).parent.parent)
TEST_ROOT_DIR: str = str(Path(__file__).parent)
TEST_DATA_DIR: str = str(Path(TEST_ROOT_DIR) / "data")


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

    def users_list(self, *args: Any, **kwrags: Any) -> SlackResponse:
        with open(os.path.join(TEST_DATA_DIR, "web_response_users_list.json")) as f:
            web_response: Dict = json.load(f)
            return get_slackresponse(web_response)

    def conversations_history(self, *args: Any, **kwrags: Any) -> SlackResponse:
        with open(
            os.path.join(TEST_DATA_DIR, "web_response_conversations_history.json")
        ) as f:
            web_response: Dict = json.load(f)
            return get_slackresponse(web_response)

    def chat_getPermalink(
        self, *, channel: str, message_ts: str, **kwargs: Any
    ) -> SlackResponse:
        with open(
            os.path.join(TEST_DATA_DIR, "web_response_chat_getPermalink.json")
        ) as f:
            web_response: Dict = json.load(f)
            return get_slackresponse(web_response)

    def conversations_join(self, *, channel: str, **kwargs: Any) -> SlackResponse:
        with open(
            os.path.join(TEST_DATA_DIR, "web_response_conversations_join.json")
        ) as f:
            web_response: Dict = json.load(f)
            return get_slackresponse(web_response)

    def conversations_archive(self, *, channel: str, **kwargs: Any) -> SlackResponse:
        with open(
            os.path.join(TEST_DATA_DIR, "web_response_conversations_archive.json")
        ) as f:
            web_response: Dict = json.load(f)
            return get_slackresponse(web_response)

    def chat_postMessage(
        self, *, channel: str, text: Optional[str] = None, **kwargs: Any
    ) -> SlackResponse:
        with open(
            os.path.join(TEST_DATA_DIR, "web_response_chat_postMessage.json")
        ) as f:
            web_response: Dict = json.load(f)
            return get_slackresponse(web_response)
