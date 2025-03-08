from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage


class HomePageLocators:
    """
    Contains locators for elements on the Home Page.
    """
    HEADER_LOGO: tuple[str, str] = (By.XPATH, "//img[@class='gapmap-logo large-sc-hide ng-star-inserted']")
    LOGIN_BUTTON: tuple[str, str] = (By.CLASS_NAME, "login-btn")


class HomePage(BasePage):
    """
    Page Object Model for the Home Page.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Initialize the HomePage with a Selenium WebDriver instance.

        Args:
            driver (WebDriver): The Selenium WebDriver instance.
        """
        self.driver: WebDriver = driver
        super().__init__(driver)

    # Navigation

    def go_to_login_page(self) -> None:
        """
        Navigate to the login page by clicking the login button.

        Returns:
            None
        """
        self.click(HomePageLocators.LOGIN_BUTTON)

    # Assertions

    def is_header_logo_present(self) -> bool:
        """
        Verify that the header logo is present on the Home Page.

        Waits for the header logo element to be visible and asserts it is displayed.

        Returns:
            bool: True if the header logo is displayed, otherwise an AssertionError is raised.
        """
        self.wait_for_element(HomePageLocators.HEADER_LOGO)
        return self.assert_that(HomePageLocators.HEADER_LOGO).is_displayed()
