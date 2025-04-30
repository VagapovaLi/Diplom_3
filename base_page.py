import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.base_page_locators import BasePageLocators

class BasePage:
    def __init__(self, driver,timeout=20):
        self.driver = driver
        self.timeout = timeout


    @allure.step('Открываем страницу: {url}')
    def open(self, url):
        self.driver.get(url)


    @allure.step('Нажимаем на кнопку "Личный кабинет" на главной странице')
    def click_button_personal_account(self):
        WebDriverWait(self.driver,  10).until(
            EC.element_to_be_clickable(BasePageLocators.BUTTON_PERSONAL_ACCOUNT)
        ).click()
