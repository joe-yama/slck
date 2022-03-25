from slck.utils import confirm_user_input


def test__confirm_user_input() -> None:
    assert confirm_user_input(question="test", answer="yes")
