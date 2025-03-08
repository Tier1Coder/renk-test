from configuration.test_driver import TestDriver


def test_invalid_login():
    with TestDriver() as TD:
        TD.home_page.go_to_login_page()
        TD.authentication_page.fill_login_form(
            "abcd", "zgesgseges="
        )
        TD.authentication_page.click_login_button()
        TD.authentication_page.is_user_not_found_displayed()
