import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.base_page_locators import BasePageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

class BasePage:

    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.timeout = timeout

    @allure.step('Открываем страницу: {url}')
    def open(self, url):
        self.driver.get(url)


    @allure.step('Получаем текущий URL')
    def get_current_url(self):
        return self.driver.current_url
    def wait_element_disappears(self, how, what):
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.invisibility_of_element_located((how, what)))
        except TimeoutException:
            raise TimeoutException(f'Modal window did not hide after {self.timeout} seconds')

    @allure.step('Получить текст')
    def get_text(self, locator):
        actually_text = self.driver.find_element(*locator).text
        return actually_text

    def find_clickable_element(self, how, what):
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            raise TimeoutException(f'\nElement not clickable after {self.timeout} seconds')

    def find_visibility_element(self, how, what):
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            raise TimeoutException(f'\nElement not visibility after {self.timeout} seconds')

    def presence_of_elements(self, how, what):
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located((how, what)))
        except TimeoutException:
            raise TimeoutException(f'\nElements not present after {self.timeout} seconds')


    @allure.step("Ожидание кликабельного элемента на странице")
    def wait_element_to_be_clickable(self, how, what):
        return self.find_clickable_element(how, what)

    @allure.step("Ожидание видимости элемента на странице")
    def visibility_of_element(self, how, what):
        return self.find_visibility_element(how, what)

    @allure.step('Нажимаем на заказ')
    def click_button_order_feed(self):
        self.find_clickable_element(*BasePageLocators.BUTTON_ORDER_FEED).click()

    @allure.step('Переместиться к элементу и кликнуть')
    def move_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    @allure.step('Нажимаем на кнопку "Личный кабинет" на главной странице')
    def click_button_personal_account(self):
        self.find_clickable_element(*BasePageLocators.BUTTON_PERSONAL_ACCOUNT).click()

    @allure.step('Найти элемент на странице')
    def find_element_on_page(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    @allure.step('Найти элемент и кликнуть по нему')
    def find_element_and_click(self, how, what):
        self.find_clickable_element(how, what).click()


    def text_present_in_element(self, how, what, text):
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.text_to_be_present_in_element((how, what), text))
        except TimeoutException:
            raise TimeoutException(f'\nElement not present in element after {self.timeout} seconds')


    @allure.step('Перетащить элемент')
    def drag_and_drop(self, how_s, what_s, how_t, what_t):
        source = self.find_clickable_element(how_s, what_s)
        target = self.find_visibility_element(how_t, what_t)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()

    @allure.step('Переместиться к элементу и кликнуть')
    def move_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()


    @allure.step('Нажимаем на кнопку "Конструктор" на главной странице')
    def click_button_link_constructor(self):
        self.find_clickable_element(*BasePageLocators.BUTTON_CONSTRUCTOR).click()

    @allure.step('Нажимаем на кнопку "Лента заказов" на главной странице')
    def click_button_order_feed(self):
        self.find_element_and_click(*BasePageLocators.BUTTON_ORDER_FEED)