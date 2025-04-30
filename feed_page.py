import allure

from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
class FeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)




