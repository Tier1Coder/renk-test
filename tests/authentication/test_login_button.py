from configuration.test_driver import TestDriver


def test_login_button():
    with TestDriver() as TD:
        TD.home_page.go_to_login_page()
        TD.authentication_page.is_login_button_displayed()
