from configuration.test_driver import TestDriver


def test_is_header_logo_present():
    with TestDriver() as TD:
        TD.home_page.is_header_logo_present()
