from pages.base_page import BasePage
from playwright.sync_api import Locator
from playwright.sync_api import Page

class AuthPage(BasePage):
    """Page to test login in Saucedemo"""

    def __init__(self, page: Page) -> None:
        """Initialize TestAuthPage"""
        super().__init__(page)
        self._username_input: Locator = self.page.get_by_placeholder("Username")
        self._password_input: Locator = self.page.get_by_placeholder("Password")
        self._login_button: Locator = self.page.get_by_role("button", name="Login")
        self._error_message_container: Locator = self.page.locator("[data-test='error']")

    def execute_login(self, username_value: str, password_value: str) -> None:
        """
        Execute the sequential login execution flow.
        """

        self._username_input.fill(username_value)
        self._password_input.fill(password_value)
        self._login_button.click()

    @property
    def get_error_message_element(self) -> Locator:
       return self._error_message_container