import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
#from data import LoginData
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Нажимаем на кнопку "Восстановить пароль"')
    def click_restore_password(self):

        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(LoginPageLocators.BUTTON_RECOVER_PASSWORD)
        ).click()

