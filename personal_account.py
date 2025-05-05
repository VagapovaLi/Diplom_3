import allure
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from locators.personal_account_locators import PersonalAccountPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.base_page_locators import BasePageLocators


class PersonalAccountPage(BasePage):
    def __init__(self, driver,timeout=20):
        super().__init__(driver)
        self.timeout = timeout


    @allure.step('Проверяем что есть подсказка для личного кабинета и возвращаем текущий URL')
    def additional_info_personal_account_and_return_current_url(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PersonalAccountPageLocators.LABEL_PERSONAL_ACCOUNT))
        return self.driver.current_url

    @allure.step('Нажимаем на кнопку "История заказоа" в личном кабинете')
    def click_button_order_history(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(PersonalAccountPageLocators.BUTTON_ORDER_HISTORY)
        ).click()

    @allure.step('Нажимаем на кнопку "Выход"')
    def click_button_exit(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(PersonalAccountPageLocators.BUTTON_EXIT)
        ).click()


    @allure.step('Получаем номер последнего заказа')
    def get_last_order_data(self):

        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(PersonalAccountPageLocators.LIST_OF_ORDERS)
        ).text


