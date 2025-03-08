import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from decouple import config
from typing import Optional, Type
from types import TracebackType

from pages.user_profile_page import UserProfilePage
from pages.authentication_page import AuthenticationPage
from pages.home_page import HomePage
from pages.ticket_page import TicketPage
from utils.helpers import get_test_context_from_stack



class TestDriver:
    """
    A context manager for managing a headless Selenium Chrome WebDriver session
    for automated testing. It navigates to a specified URL and provides access to
    various page objects. On exit, it captures a screenshot with a filename composed
    of the test context and a timestamp, then quits the driver.

    Attributes:
        url (str): The URL to load. Defaults to the TEST_URL from environment variables.
        driver (WebDriver): The Selenium WebDriver instance.
    """

    def __init__(self, url: Optional[str] = None) -> None:
        self.url = url if url else config("TEST_URL")
        self.driver = None

    def __enter__(self) -> "TestDriver":
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(self.url)
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        exc_traceback: Optional[TracebackType]
    ) -> None:
        if self.driver:
            folder_name, test_name = get_test_context_from_stack()
            if not test_name:
                test_name = "no_test_name"
            if not folder_name:
                folder_name = "no_folder"
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            screenshots_dir = os.path.join(project_root, "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            screenshot_filename = f"{folder_name}_{test_name}_{timestamp}.png"
            screenshot_path = os.path.join(screenshots_dir, screenshot_filename)
            self.driver.save_screenshot(screenshot_path)
            self.driver.quit()

    @property
    def home_page(self) -> HomePage:
        return HomePage(self.driver)

    @property
    def authentication_page(self) -> AuthenticationPage:
        return AuthenticationPage(self.driver)

    @property
    def user_profile_page(self) -> UserProfilePage:
        return UserProfilePage(self.driver)

    @property
    def ticket_page(self) -> TicketPage:
        return TicketPage(self.driver)
