import time

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from data import LoginData

class LoginPage(BasePage):
    def __init__(self, driver,timeout=20):
        super().__init__(driver)
        self.timeout = timeout


    @allure.step('Нажимаем на кнопку "Восстановить пароль"')
    def click_restore_password(self):

        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(LoginPageLocators.BUTTON_RECOVER_PASSWORD)
        ).click()

    @allure.step('Заполняем поле "Email"')
    def input_email(self):
        email_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.INPUT_EMAIL)
        )
        email_input.send_keys(LoginData.DEFAULT_USER.get('email'))

    @allure.step('Заполняем поле "Пароль"')
    def input_password(self):
        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.INPUT_PASSWORD)
        )
        password_input.send_keys(LoginData.DEFAULT_USER.get('password'))

    @allure.step('Нажимаем кнопку "Войти"')
    def click_button_login(self):
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(LoginPageLocators.BUTTON_LOGIN)
        ).click()

    @allure.step('Выполняем авторизацию пользователя')
    def authorization_user_data(self):
        self.input_email()
        self.input_password()
        time.sleep(5)
        self.click_button_login()



    @allure.step('Переход на страницу "Авторзации"')
    def go_to_page_authorization_and_return_current_url(self):

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.BUTTON_LOGIN)
        )
        return self.driver.current_url
