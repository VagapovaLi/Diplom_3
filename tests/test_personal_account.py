import allure
import urls
from pages.personal_account import PersonalAccountPage
from pages.login_page import LoginPage
import time


class TestPersonalAccount:
    @allure.title('Перехода по клику на "Личный кабинет"')
    def test_click_go_to_personal_account(self,driver, auth_user):
        personal_account = PersonalAccountPage(driver)
        time.sleep(5)
        personal_account.click_button_personal_account()
        current_url =personal_account.additional_info_personal_account_and_return_current_url()
        assert current_url == urls.ACCOUNT_PROFILE_URL

    @allure.title('Перехода в раздел  "История заказов"')
    def test_click_go_to_order_history(self, driver, auth_user):
        personal_account = PersonalAccountPage(driver)
        time.sleep(5)
        personal_account.click_button_personal_account()
        personal_account.click_button_order_history()
        current_url =personal_account.additional_info_personal_account_and_return_current_url()
        assert current_url == urls.ORDER_HISTORY_URL

    @allure.title('Выход из "Личный кабинет"')
    def test_exit_personal_account(self, driver, auth_user):
        personal_account = PersonalAccountPage(driver)
        time.sleep(5)
        personal_account.click_button_personal_account()
        personal_account.click_button_exit()
        login_page = LoginPage(driver)
        current_url = login_page.go_to_page_authorization_and_return_current_url()
        assert current_url  == urls.LOGIN_URL
