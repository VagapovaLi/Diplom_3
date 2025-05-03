import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.base_page_locators import BasePageLocators
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

class BasePage:
    DEFAULT_TIMEOUT = 5
    def __init__(self, driver):
        self.driver = driver


    @allure.step('Открываем страницу: {url}')
    def open(self, url, wait_seconds=2):
        self.driver.get(url)
        if wait_seconds > 0:
            time.sleep(wait_seconds)

    @allure.step("Ожидание кликабельного элемента на странице")
    def wait_element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    @allure.step("Ожидание видимости элемента на странице")
    def visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step('Перетащить элемент')
    def drag_and_drop_to_element(self, from_locator, to_locator):
        draggable = self.driver.find_element(*from_locator)
        droppable = self.driver.find_element(*to_locator)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(draggable, droppable).perform()



    @allure.step('Нажимаем на кнопку "Личный кабинет" на главной странице')

    def click_button_personal_account(self):
        self.wait_element_visible(BasePageLocators.BUTTON_PERSONAL_ACCOUNT).click()
        self.wait_element_visible(BasePageLocators.EXIT_BUTTON)
        return BasePage(self.driver)

        #self.find_clickable_element(*BasePageLocators.BUTTON_PERSONAL_ACCOUNT).click()


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

    def wait_element_visible(self, locator):
        return WebDriverWait(self.driver, self.DEFAULT_TIMEOUT).until(EC.visibility_of_element_located(locator))