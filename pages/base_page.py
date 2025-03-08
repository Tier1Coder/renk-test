from typing import Tuple, Any, Callable
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    """
    BasePage encapsulates common Selenium WebDriver interactions for page objects.
    It provides methods to click elements, fill input fields, wait for elements,
    and perform assertions on elements.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Initialize the BasePage with a Selenium WebDriver instance.

        Args:
            driver (WebDriver): The Selenium WebDriver instance.
        """
        self.driver: WebDriver = driver

    def click(self, locator: Tuple[str, str], timeout: int = 10) -> None:
        """
        Click an element after waiting for it to be clickable.

        Args:
            locator (Tuple[str, str]): Locator tuple to find the element.
            timeout (int, optional): Maximum time to wait for the element. Defaults to 10.
        """
        element: WebElement = self.wait_for_element(
            locator, exp_con=ec.element_to_be_clickable, timeout=timeout
        )
        element.click()

    def click_with_action_chains(self, locator: Tuple[str, str], timeout: int = 10) -> None:
        """
        Click an element using ActionChains. Useful for complex elements like dropdowns or hover menus.

        Args:
            locator (Tuple[str, str]): Locator tuple to find the element.
            timeout (int, optional): Maximum time to wait for the element. Defaults to 10.
        """
        element: WebElement = self.wait_for_element(
            locator, exp_con=ec.element_to_be_clickable, timeout=timeout
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def fill(self, locator: Tuple[str, str], text: str, clear_first: bool = True) -> None:
        """
        Fill an input field with text after waiting for it to be clickable.

        Args:
            locator (Tuple[str, str]): Locator tuple to find the input element.
            text (str): The text to enter.
            clear_first (bool, optional): Whether to clear the field before typing. Defaults to True.
        """
        element: WebElement = self.wait_for_element(
            locator, exp_con=ec.element_to_be_clickable, timeout=10
        )
        if clear_first:
            element.clear()
        element.send_keys(text)

    def wait_for_element(
        self,
        locator: Tuple[str, str],
        exp_con: Callable[[Tuple[str, str]], Any] = ec.visibility_of_element_located,
        timeout: int = 10,
    ) -> WebElement:
        """
        Wait for an element to meet a specified expected condition.

        Args:
            locator (Tuple[str, str]): Locator tuple to find the element.
            exp_con (Callable[[Tuple[str, str]], Any], optional): Expected condition function.
                Defaults to ec.visibility_of_element_located.
            timeout (int, optional): Maximum time to wait for the element. Defaults to 10.

        Returns:
            WebElement: The located web element once the expected condition is satisfied.
        """
        return WebDriverWait(self.driver, timeout).until(exp_con(locator))

    def assert_that(self, locator: Tuple[str, str]) -> "AssertionWrapper":
        """
        Wrap an element in an AssertionWrapper to perform assertions.

        Args:
            locator (Tuple[str, str]): Locator tuple to find the element.

        Returns:
            AssertionWrapper: A wrapper for making assertions on the element.
        """
        element: WebElement = self.wait_for_element(locator)
        return AssertionWrapper(element)


class AssertionWrapper:
    """
    AssertionWrapper provides assertion methods on a WebElement.
    """

    def __init__(self, element: WebElement) -> None:
        """
        Initialize the AssertionWrapper with a web element.

        Args:
            element (WebElement): The web element to assert upon.
        """
        self.element: WebElement = element

    def is_displayed(self) -> bool:
        """
        Assert that the wrapped element is displayed.

        Raises:
            AssertionError: If the element is not visible.

        Returns:
            bool: True if the element is displayed.
        """
        if not self.element.is_displayed():
            raise AssertionError(ElementNotVisibleException(str(self.element)))
        return True
