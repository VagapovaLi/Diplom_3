import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from pages.base_page import BasePage
import time

class PasswordRecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Проверяем наличие кнопки "Восстановить" и возвращаем текущий URL')
    def find_button_restore_return_url(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(PasswordRecoveryPageLocators.BUTTON_RECOVER))
        return self.driver.current_url


    @allure.step('Вводим email')
    def click_enter_email(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(PasswordRecoveryPageLocators.EMAIL_INPUT)
        ).click()
        time.sleep(3)
        self.driver.find_element(*PasswordRecoveryPageLocators.BUTTON_RECOVER).send_keys('dsdsds@mail.ru')

    @allure.step('Нажимаем на кнопку "Восстановить" в форме "Восстановление пароля"')
    def click_restore(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(PasswordRecoveryPageLocators.BUTTON_RECOVER)
        ).click()

    @allure.step('Проверяем наличие кнопки "Сохранить" и возвращаем текущий URL')
    def find_button_save_return_url(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(PasswordRecoveryPageLocators.BUTTON_SAVE))
        return self.driver.current_url

    @allure.step('Вводим пароль')
    def click_enter_password(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(PasswordRecoveryPageLocators.PASSWORD_INPUT)
        ).click()
        time.sleep(3)
        self.driver.find_element(*PasswordRecoveryPageLocators.PASSWORD_INPUT).send_keys('1a1s1s1d')

    @allure.step('Нажимаем на кнопку показать/скрыть пароль')
    def click_button_show_password(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(PasswordRecoveryPageLocators.BUTTON_SHOW_PASSWORD)
        ).click()

    @allure.step('Проверка что поле "Пароль" активно')
    def password_field_is_active(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(PasswordRecoveryPageLocators.ACTIVE_INPUT_PASSWORD)
        ).is_displayed()