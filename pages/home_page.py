from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePageLocators:
    HEADER_LOGO = (By.XPATH, "//img[@class='gapmap-logo large-sc-hide ng-star-inserted']")


class HomePage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def is_header_logo_present(self):
        self.wait_for_element(HomePageLocators.HEADER_LOGO, ec=ec.visibility_of_element_located, timeout=10)
        self.assert_that(HomePageLocators.HEADER_LOGO).is_displayed()


