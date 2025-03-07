from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.home_page import HomePage
from decouple import config


class TestDriver:

    def __init__(self, url: str = None):
        self.driver = webdriver.Chrome()
        self.url = url if url else config('TEST_URL')

    def __enter__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(self.url)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.driver.save_screenshot('screenshot.png')
        self.driver.quit()

    @property
    def home_page(self):
        return HomePage(self.driver)

