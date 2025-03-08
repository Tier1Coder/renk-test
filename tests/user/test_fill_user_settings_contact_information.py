from configuration.test_driver import TestDriver


def test_fill_contact_information():
    with TestDriver() as TD:
        TD.home_page.go_to_login_page()

        TD.authentication_page.fill_login_form("Testowy_1", "zadanie03Testowe2025=")
        TD.authentication_page.click_login_button()

        TD.user_profile_page.go_to_user_settings()

        TD.user_profile_page.fill_profile_form(
            last_name="Kowalski",
            first_name="Jan",
            email="jan.kowalski@example.com",
            phone_number="123456789",
            city="Warszawa",
            street="Kwiatowa",
            building="10",
            apartment_number="2",
            postal_code="00-001"
        )

        TD.user_profile_page.is_save_button_disabled()