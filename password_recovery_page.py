import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from pages.base_page import BasePage


class PasswordRecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)



    @allure.step('Проверяем наличие кнопки "Восстановить" и возвращаем текущий URL')
    def find_button_restore_return_url(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(PasswordRecoveryPageLocators.BUTTON_RECOVER))
        return self.driver.current_url


    @allure.step('Вводим email')
    def click_enter_email(self):


        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(PasswordRecoveryPageLocators.EMAIL_INPUT)
        ).click()
        self.driver.find_element(*PasswordRecoveryPageLocators.BUTTON_RECOVER).send_keys('dsdsds@mail.ru')


