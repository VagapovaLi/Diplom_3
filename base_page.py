import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.base_page_locators import BasePageLocators
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

class BasePage:

    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.timeout = timeout

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

    @allure.step('Получить текст')
    def get_text(self, locator):
        actually_text = self.driver.find_element(*locator).text
        return actually_text

    def find_clickable_element(self, how, what):
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            raise TimeoutException(f'\nElement not clickable after {self.timeout} seconds')

    def find_visability_element(self, how, what):
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            raise TimeoutException(f'\nElement not visability after {self.timeout} seconds')

    def wait_element_disappears(self, how, what):
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.invisibility_of_element_located((how, what)))
        except TimeoutException:
            raise TimeoutException(f'Modal window did not hide after {self.timeout} seconds')

    @allure.step('Перетащить элемент')
    def drag_and_drop(self, how_s, what_s, how_t, what_t):
        source = self.find_clickable_element(how_s, what_s)
        target = self.find_visability_element(how_t, what_t)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()

    @allure.step('Переместиться к элементу и кликнуть')
    def move_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    @allure.step('Нажимаем на кнопку "Личный кабинет" на главной странице')


    def click_button_per_account(self):
        self.find_clickable_element(*BasePageLocators.BUTTON_PERSONAL_ACCOUNT).click()

    def click_button_personal_account(self):
        # self.wait_element_visible(BasePageLocators.BUTTON_PERSONAL_ACCOUNT).click()
        # self.wait_element_visible(BasePageLocators.EXIT_BUTTON)
        # return BasePage(self.driver)

        self.find_clickable_element(*BasePageLocators.BUTTON_PERSONAL_ACCOUNT).click()


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

    # def wait_element_visible(self, locator):
    #     return WebDriverWait(self.driver, self.DEFAULT_TIMEOUT).until(EC.visibility_of_element_located(locator))
    #
    # def text_present_in_element(self, how, what, text):
    #     try:
    #         return WebDriverWait(self.driver, self.timeout).until(EC.text_to_be_present_in_element((how, what), text))
    #     except TimeoutException:
    #         raise TimeoutException(f'\nElement not present in element after {self.timeout} seconds')