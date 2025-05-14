import allure
import urls
from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecoveryPage


class TestPasswordRecovery:
    @allure.title('Перехода на страницу восстановление пароля" по кнопк  "Восстановить пароль"')
    def test_go_page_password_recovery_clicking_recover_password(self,driver):
        login_page = LoginPage(driver)
        login_page.open(urls.LOGIN_URL)
        login_page.click_restore_password()
        password_recovery_page = PasswordRecoveryPage(driver)
        current_url = password_recovery_page.find_button_restore_return_url()
        assert current_url == urls.PASSWORD_RECOVERY

    @allure.title('Ввод почты и клик по кнопке "Восстановить"  в форме "Восстановления пароля"')
    def test_enter_email_click_restore(self,driver):
        login_page = LoginPage(driver)
        login_page.open(urls.LOGIN_URL)
        login_page.click_restore_password()
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.click_enter_email()
        password_recovery_page.click_restore()
        current_url = password_recovery_page.find_button_save_return_url()
        assert current_url == urls.RESET_PASSWORD_URL

    @allure.title('Нажать на кнопку показать/скрыть пароль, проверка подсветки')
    def test_enter_show_hide_password_and_backlight(self,driver):
        login_page = LoginPage(driver)
        login_page.open(urls.LOGIN_URL)
        login_page.click_restore_password()
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.click_enter_email()
        password_recovery_page.click_restore()
        password_recovery_page.click_enter_password()
        password_recovery_page.click_button_show_password()
        assert password_recovery_page.password_field_is_active()