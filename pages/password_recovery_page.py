import allure
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from pages.base_page import BasePage
from data import LoginData

class PasswordRecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Проверяем наличие кнопки "Восстановить" и возвращаем текущий URL')
    def find_button_restore_return_url(self):
        self.find_clickable_element(*PasswordRecoveryPageLocators.BUTTON_RECOVER)
        return self.get_current_url()


    @allure.step('Вводим email')
    def click_enter_email(self,email=LoginData.DEFAULT_USER.get('email')):
        self.find_clickable_element(*PasswordRecoveryPageLocators.EMAIL_INPUT).send_keys(email)


    @allure.step('Нажимаем на кнопку "Восстановить" в форме "Восстановление пароля"')
    def click_restore(self):
        self.find_clickable_element(*PasswordRecoveryPageLocators.BUTTON_RECOVER).click()


    @allure.step('Проверяем наличие кнопки "Сохранить" и возвращаем текущий URL')
    def find_button_save_return_url(self):
        self.find_clickable_element(*PasswordRecoveryPageLocators.BUTTON_SAVE)
        return self.get_current_url()

    @allure.step('Вводим пароль')
    def click_enter_password(self,password=LoginData.DEFAULT_USER.get('password')):
        self.find_clickable_element(*PasswordRecoveryPageLocators.PASSWORD_INPUT).send_keys(password)


    @allure.step('Нажимаем на кнопку показать/скрыть пароль')
    def click_button_show_password(self):
        self.find_clickable_element(*PasswordRecoveryPageLocators.BUTTON_SHOW_PASSWORD).click()


    @allure.step('Проверка что поле "Пароль" активно')
    def password_field_is_active(self):
        return self.find_visibility_element(*PasswordRecoveryPageLocators.ACTIVE_INPUT_PASSWORD).is_displayed()

