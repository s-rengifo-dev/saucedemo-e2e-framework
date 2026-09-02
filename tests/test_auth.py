import re
import pytest
from config import USER, PASSWORD
from pages.auth_page import AuthPage
from playwright.sync_api import expect


def test_successful_login(auth_page: AuthPage) -> None:
    """Verify that a user can log in successfully with valid credentials."""

    auth_page.execute_login(USER, PASSWORD)

    expect(auth_page.page).to_have_url(re.compile(r"/inventory\.html$"))

@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("locked_out_user", PASSWORD, "Epic sadface: Sorry, this user has been locked out."),
        ("user_not_registered", PASSWORD, "Epic sadface: Username and password do not match any user in this service"),
        (USER, "wrong_password", "Epic sadface: Username and password do not match any user in this service"),
        (USER, "", "Epic sadface: Password is required"),
        ("", PASSWORD, "Epic sadface: Username is required"),
        ("", "", "Epic sadface: Username is required")

    ]  
)

def test_login_wrong_states(auth_page: AuthPage, username: str, password: str, expected_error: str) -> None:
    """Verify that a user can't log in successfully with invalid credentials."""

    auth_page.execute_login(username, password)
    expect(auth_page.get_error_message_element).to_contain_text(expected_error)
