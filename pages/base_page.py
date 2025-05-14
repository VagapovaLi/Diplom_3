import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.base_page_locators import BasePageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.timeout = timeout

    @allure.step('Открываем страницу: {url}')
    def open(self, url):
        self.driver.get(url)


    @allure.step('Ожидание появления элемента на странице')
    def wait_for_element(self, how, what):
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            raise TimeoutException(f'Element not visible after {self.timeout} seconds')

    @allure.step('Получаем текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Получаем элемент')
    def get_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step('Получить текст элемента')
    def get_text(self, how, what):
        try:
            self.wait_for_element(how, what)
            actually_text = self.driver.find_element(how, what).text
            return actually_text
        except NoSuchElementException:
            raise NoSuchElementException(f'Element not found with locator: ({how}, {what})')
        except Exception as e:
            raise Exception(f'An error occurred while getting text from element: {str(e)}')

    def wait_element_disappears(self, how, what):
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.invisibility_of_element_located((how, what)))
        except TimeoutException:
            raise TimeoutException(f'Modal window did not hide after {self.timeout} seconds')

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


    @allure.step('Нажимаем на Лента Заказов')
    def click_button_order_feed(self):
        self.find_clickable_element(*BasePageLocators.BUTTON_ORDER_FEED).click()


    @allure.step('Нажимаем на кнопку "Личный кабинет" на главной странице')
    def click_button_personal_account(self):
        self.find_clickable_element(*BasePageLocators.BUTTON_PERSONAL_ACCOUNT).click()

    def text_present_in_element(self, how, what, text):
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.text_to_be_present_in_element((how, what), text))
        except TimeoutException:
            raise TimeoutException(f'\nElement not present in element after {self.timeout} seconds')


    def drag_and_drop(self, element, target):
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    @allure.step('Переместиться к элементу и кликнуть')
    def move_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()


    @allure.step('Нажимаем на кнопку "Конструктор" на главной странице')
    def click_button_link_constructor(self):
        self.find_clickable_element(*BasePageLocators.BUTTON_CONSTRUCTOR).click()

    @allure.step('Ожидание исчезновения текста в элементе')
    def wait_for_text_to_disappear(self, locator, text):
        try:
            WebDriverWait(self.driver, self.timeout).until_not(
                expected_conditions.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            raise TimeoutException(f'Text "{text}" did not disappear from element after {self.timeout} seconds')

