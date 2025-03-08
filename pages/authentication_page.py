from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AuthenticationPageLocators:
    """
    Contains locator tuples for elements on the Authentication Page.
    """
    USERNAME_FORM = (By.ID, 'username')
    PASSWORD_FORM = (By.ID, 'password')
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']//span[text()=' Zaloguj ']")
    USER_NOT_FOUND_ALERT = (By.CSS_SELECTOR, "app-server-error div[role='alert']")


class AuthenticationPage(BasePage):
    """
    Page Object Model for the Authentication Page.
    """

    def __init__(self, driver) -> None:
        """
        Initialize the AuthenticationPage with a Selenium WebDriver instance.

        Args:
            driver: Selenium WebDriver instance.
        """
        self.driver = driver
        super().__init__(driver)

    # Helper Functions

    def fill_login_form(self, login: str, password: str) -> None:
        """
        Fill the login form with provided username and password.

        Args:
            login (str): The username to be entered.
            password (str): The password to be entered.
        """
        self.fill(AuthenticationPageLocators.USERNAME_FORM, login)
        self.fill(AuthenticationPageLocators.PASSWORD_FORM, password)

    def click_login_button(self) -> None:
        """
        Click the login button to submit the login form.
        """
        self.click(AuthenticationPageLocators.LOGIN_BUTTON)

    # Assertions

    def is_user_not_found_displayed(self) -> bool:
        """
        Check if the 'user not found' alert is displayed.

        Returns:
            bool: True if the alert is displayed, False otherwise.
        """
        return self.assert_that(AuthenticationPageLocators.USER_NOT_FOUND_ALERT).is_displayed()

    def is_login_button_displayed(self) -> bool:
        """
        Check if the login button is displayed.

        Returns:
            bool: True if the login button is visible, False otherwise.
        """
        return self.assert_that(AuthenticationPageLocators.LOGIN_BUTTON).is_displayed()
