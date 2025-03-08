from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage


class UserProfilePageLocators:
    """
    Contains locators for elements on the User Profile Page.
    """
    USER_FULL_NAME: tuple[str, str] = (By.CLASS_NAME, "full-name")
    SETTINGS_BUTTON: tuple[str, str] = (By.LINK_TEXT, "Ustawienia")
    PROFILE_DETAILS: tuple[str, str] = (By.XPATH, "//th[contains(text(), 'Szczegóły profilu')]")
    LAST_NAME: tuple[str, str] = (By.XPATH, "//input[@formcontrolname='lastName']")
    FIRST_NAME: tuple[str, str] = (By.XPATH, "//input[@formcontrolname='firstName']")
    EMAIL: tuple[str, str] = (By.XPATH, "//input[@formcontrolname='email']")
    PHONE_NUMBER: tuple[str, str] = (By.XPATH, "//input[@formcontrolname='phoneNumber']")
    CITY: tuple[str, str] = (By.XPATH, "//input[@formcontrolname='city']")
    STREET: tuple[str, str] = (By.XPATH, "//input[@formcontrolname='street']")
    BUILDING: tuple[str, str] = (By.XPATH, "//input[@formcontrolname='building']")
    APARTMENT_NUMBER: tuple[str, str] = (By.XPATH, "//input[@formcontrolname='apartmentNumber']")
    POSTAL_CODE: tuple[str, str] = (By.XPATH, "//input[@formcontrolname='postalCode']")
    SAVE_BUTTON: tuple[str, str] = (
        By.XPATH,
        "//button[contains(@class, 'custom-fill-primary-btn') and span[contains(text(), 'Zapisz zmiany')]]"
    )
    TICKETS_BUTTON: tuple[str, str] = (By.XPATH, "//button[contains(., 'Bilety')]")


class UserProfilePage(BasePage):
    """
    Page Object Model for the User Profile Page.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Initialize the UserProfilePage with a Selenium WebDriver instance.

        Args:
            driver (WebDriver): The Selenium WebDriver instance.
        """
        self.driver: WebDriver = driver
        super().__init__(driver)

    # Navigation

    def go_to_user_settings(self) -> None:
        """
        Navigate to the user settings page by clicking on the user's full name and settings button.
        """
        self.click_with_action_chains(UserProfilePageLocators.USER_FULL_NAME)
        self.click_with_action_chains(UserProfilePageLocators.SETTINGS_BUTTON)

    def go_to_ticket_page(self) -> None:
        """
        Navigate to the ticket page by clicking on the tickets button.
        """
        self.click_with_action_chains(UserProfilePageLocators.TICKETS_BUTTON)

    # Helper Functions

    def fill_profile_form(
        self,
        last_name: str,
        first_name: str,
        email: str,
        phone_number: str,
        city: str,
        street: str,
        building: str,
        apartment_number: str,
        postal_code: str
    ) -> None:
        """
        Fill the user profile form with the provided data.

        Args:
            last_name (str): User's last name.
            first_name (str): User's first name.
            email (str): User's email address.
            phone_number (str): User's phone number.
            city (str): City name.
            street (str): Street name.
            building (str): Building number.
            apartment_number (str): Apartment number.
            postal_code (str): Postal code.
        """
        self.fill(UserProfilePageLocators.LAST_NAME, last_name)
        self.fill(UserProfilePageLocators.FIRST_NAME, first_name)
        self.fill(UserProfilePageLocators.EMAIL, email)
        self.fill(UserProfilePageLocators.PHONE_NUMBER, phone_number)
        self.fill(UserProfilePageLocators.CITY, city)
        self.fill(UserProfilePageLocators.STREET, street)
        self.fill(UserProfilePageLocators.BUILDING, building)
        self.fill(UserProfilePageLocators.APARTMENT_NUMBER, apartment_number)
        self.fill(UserProfilePageLocators.POSTAL_CODE, postal_code)

    # Assertions

    def is_user_logged_in(self) -> bool:
        """
        Assert that the user is logged in by verifying that the user full name is displayed.

        Returns:
            bool: True if the user full name element is displayed, otherwise an AssertionError is raised.
        """
        return self.assert_that(UserProfilePageLocators.USER_FULL_NAME).is_displayed()

    def are_profile_details_displayed(self) -> bool:
        """
        Assert that the profile details are displayed on the page.

        Returns:
            bool: True if the profile details element is displayed, otherwise an AssertionError is raised.
        """
        return self.assert_that(UserProfilePageLocators.PROFILE_DETAILS).is_displayed()

    def is_save_button_disabled(self) -> bool:
        """
        Check whether the 'Save Changes' button is disabled.

        Returns:
            bool: True if the save button is disabled.

        Raises:
            AssertionError: If the save button is not disabled.
        """
        button: WebElement = self.wait_for_element(UserProfilePageLocators.SAVE_BUTTON)
        is_disabled: str = button.get_attribute("disabled")
        assert is_disabled is not None, "The 'Zapisz zmiany' button is not disabled!"
        return True
