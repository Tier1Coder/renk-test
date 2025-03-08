from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage


class TicketPageLocators:
    """
    Contains locators for elements on the Ticket Page.
    """
    BUY_TICKET_HEADER: tuple[str, str] = (By.XPATH, "//h2[contains(text(), 'Kup bilet')]")
    TICKET_TYPE_SELECT: tuple[str, str] = (By.ID, "ticketType")
    PRICING_TAB: tuple[str, str] = (By.XPATH, "//button//span[contains(text(), 'Cennik')]")
    NEXT_BUTTON: tuple[str, str] = (By.XPATH, "//button[span[contains(text(),'Dalej')]]")
    TICKET_TYPE_OPTION: tuple[str, str] = (
        By.XPATH,
        "//tui-data-list//button[.//label[normalize-space(text())='{ticket_type}']]"
    )


class TicketPage(BasePage):
    """
    Page Object Model for the Ticket Page.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Initialize the TicketPage with a Selenium WebDriver instance.

        Args:
            driver (WebDriver): The Selenium WebDriver instance.
        """
        super().__init__(driver)

    def select_ticket_type(self, ticket_type: str) -> None:
        """
        Select a ticket type from the ticket type dropdown.

        Args:
            ticket_type (str): The type of ticket to select.
        """
        self.click_with_action_chains(TicketPageLocators.TICKET_TYPE_SELECT)
        option_locator: tuple[str, str] = (
            TicketPageLocators.TICKET_TYPE_OPTION[0],
            TicketPageLocators.TICKET_TYPE_OPTION[1].format(ticket_type=ticket_type)
        )
        self.wait_for_element(option_locator, ec.element_to_be_clickable)
        self.click_with_action_chains(option_locator)

    def click_next_button(self) -> None:
        """
        Click the 'Next' button to proceed to the next step.
        """
        self.click(TicketPageLocators.NEXT_BUTTON)

    def is_pricing_step_displayed(self) -> bool:
        """
        Verify that the pricing step is displayed on the Ticket Page.

        Returns:
            bool: True if the pricing tab is displayed, otherwise an AssertionError is raised.
        """
        return self.assert_that(TicketPageLocators.PRICING_TAB).is_displayed()
