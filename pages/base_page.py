from playwright.sync_api import Page
from playwright.sync_api import Locator

class BasePage:
    """Base Page holding the Playwright Page instance."""

    def __init__(self, page: Page) -> None:
        self.page = page

    def wait_for_ready(self) -> None:
        self.page.wait_for_load_state("domcontentloaded")
