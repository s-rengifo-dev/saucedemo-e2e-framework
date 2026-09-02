import pytest
from playwright.sync_api import Page
from pages.auth_page import AuthPage

from config import BASE_URL

@pytest.fixture
def auth_page(page: Page) -> AuthPage:
    """
    Function to redirect to login page from saucedemo.com
    """
    page.goto(BASE_URL)
    return AuthPage(page)