from configuration.test_driver import TestDriver


def test_is_pricing_step_displayed():
    with TestDriver() as TD:
        TD.home_page.go_to_login_page()
        TD.authentication_page.fill_login_form("Testowy_1", "zadanie03Testowe2025=")
        TD.authentication_page.click_login_button()
        TD.user_profile_page.go_to_ticket_page()
        TD.ticket_page.select_ticket_type("BILET CZASOWY")
        TD.ticket_page.click_next_button()
        TD.ticket_page.is_pricing_step_displayed()
