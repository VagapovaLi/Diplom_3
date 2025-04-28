import allure
import urls
from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecoveryPage
import time

class TestPasswordRecovery:
    @allure.title('Перехода на страницу восстановление пароля" по кнопк  "Восстановить пароль"')
    def test_go_page_password_recovery_clicking_recover_password(self,driver):
        login_page = LoginPage(driver)
        time.sleep(3)
        login_page.open(urls.LOGIN_URL)
        time.sleep(3)
        login_page.click_restore_password()
        time.sleep(3)
        password_recovery_page = PasswordRecoveryPage(driver)
        time.sleep(3)
        current_url = password_recovery_page.find_button_restore_return_url()
        time.sleep(3)
        assert current_url == urls.PASSWORD_RECOVERY

    @allure.title('Ввод почты и клик по кнопке "Восстановить"  в форме "Восстановления пароля"')
    def test_enter_email_click_restore(self,driver):
        login_page = LoginPage(driver)
        login_page.open(urls.LOGIN_URL)
        login_page.click_restore_password()
        password_recovery_page = PasswordRecoveryPage(driver)
        time.sleep(3)
        #current_url = password_recovery_page.find_button_restore_return_url()
        password_recovery_page.click_enter_email()
        time.sleep(5)