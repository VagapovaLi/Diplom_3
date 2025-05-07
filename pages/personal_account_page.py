import allure
from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountPageLocators


class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверяем что есть подсказка для личного кабинета и возвращаем текущий URL')
    def additional_info_personal_account_and_return_current_url(self):
        self.find_visibility_element(*PersonalAccountPageLocators.LABEL_PERSONAL_ACCOUNT)
        return self.get_current_url()


    @allure.step('Нажимаем на кнопку "История заказоа" в личном кабинете')
    def click_button_order_history(self):
        self.find_clickable_element(*PersonalAccountPageLocators.BUTTON_ORDER_HISTORY).click()


    @allure.step('Нажимаем на кнопку "Выход"')
    def click_button_exit(self):
        self.find_clickable_element(*PersonalAccountPageLocators.BUTTON_EXIT).click()


    @allure.step('Получаем номер последнего заказа')
    def get_last_order_data(self):
        return self.find_visibility_element(*PersonalAccountPageLocators.LIST_OF_ORDERS).text
