from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, by, locator):
        try:
            return self.driver.find_element(by, locator)
        except NoSuchElementException as e:
            raise NoSuchElementException(f"Element not found: '{locator}' (by {by})") from e

    def find_all(self, by, locator):
        return self.driver.find_elements(by, locator)

    def click(self, by, locator):
        element = self.find(by, locator)
        element.click()

    def fill(self, by, locator, text, clear_first=True):
        element = self.find(by, locator)
        if clear_first:
            element.clear()
        element.send_keys(text)

    def get_text(self, by, locator):
        element = self.find(by, locator)
        return element.text

    def wait_for_element(self, locator, ec, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec(locator))


    def assert_that(self, locator):

        element = self.find(*locator)
        return AssertionWrapper(element)


class AssertionWrapper:
    def __init__(self, element):
        self.element = element

    def is_displayed(self):
        if not self.element.is_displayed():
            raise AssertionError(ElementNotVisibleException(self.element))
        return True