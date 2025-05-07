import allure
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from data import LoginData

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Нажимаем на кнопку "Восстановить пароль"')
    def click_restore_password(self):
        self.find_clickable_element(*LoginPageLocators.BUTTON_RECOVER_PASSWORD).click()

    @allure.step('Заполняем поле "Email"')
    def input_email(self):
        self.find_clickable_element(*LoginPageLocators.INPUT_EMAIL).send_keys(LoginData.DEFAULT_USER.get('email'))

    @allure.step('Заполняем поле "Пароль"')
    def input_password(self):
        self.find_clickable_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(LoginData.DEFAULT_USER.get('password'))

    @allure.step('Нажимаем кнопку "Войти"')
    def click_button_login(self):
        self.find_clickable_element(*LoginPageLocators.BUTTON_LOGIN).click()

    @allure.step('Выполняем авторизацию пользователя')
    def authorization_user_data(self):
        self.input_email()
        self.input_password()
        self.click_button_login()

    @allure.step('Переход на страницу "Авторзации"')
    def go_to_page_authorization_and_return_current_url(self):
        self.find_visibility_element(*LoginPageLocators.BUTTON_LOGIN)
        return self.get_current_url()
