import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.base_page_locators import BasePageLocators
import time


class BasePage:
    def __init__(self, driver,timeout=20):
        self.driver = driver
        self.timeout = timeout



    @allure.step('Открываем страницу: {url}')
    def open(self, url, wait_seconds=2):
        self.driver.get(url)
        if wait_seconds > 0:
            time.sleep(wait_seconds)

    @allure.step('Нажимаем на кнопку "Личный кабинет" на главной странице')
    def click_button_personal_account(self):
        WebDriverWait(self.driver,  10).until(
            EC.element_to_be_clickable(BasePageLocators.BUTTON_PERSONAL_ACCOUNT)
        ).click()


    @allure.step('Нажимаем на кнопку "Конструктор" на главной странице')
    def click_button_link_constructor(self):
        WebDriverWait(self.driver,  10).until(
            EC.element_to_be_clickable(BasePageLocators.BUTTON_CONSTRUCTOR)
        ).click()


    @allure.step('Нажимаем на кнопку "Лента заказов" на главной странице')
    def click_button_order_feed(self):
        button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(BasePageLocators.BUTTON_ORDER_FEED)
        )

        # Клик с помощью JavaScript
        self.driver.execute_script("arguments[0].click();", button)

        #WebDriverWait(self.driver,  20).until(
            #EC.element_to_be_clickable(BasePageLocators.BUTTON_ORDER_FEED)
        #).click()
