from configuration.test_driver import TestDriver


def test_invalid_login():
    with TestDriver() as TD:
        TD.home_page.go_to_login_page()
        TD.authentication_page.fill_login_form(
            "Testowy_1", "zadanie03Testowe2025="
        )
        TD.authentication_page.click_login_button()
        TD.user_profile_page.is_user_logged_in()
