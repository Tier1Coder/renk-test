from configuration.test_driver import TestDriver


def test_header_logo_is_present():
    with TestDriver() as TD:
        TD.home_page.is_header_logo_present()
