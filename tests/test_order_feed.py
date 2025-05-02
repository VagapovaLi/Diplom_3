import time

import allure
import pytest

import urls
from pages.feed_page import FeedPage
from pages.home_page import HomePage
from pages.personal_account import PersonalAccountPage


@pytest.mark.feed_page
@allure.feature('Страница "Лента заказов"')
class TestFeedOrders:
    @allure.title('Авторизованный пользователь оформил заказ')
    def test_authorized_user_placed_order(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open(urls.FEED_URL, wait_seconds=3)
        feed_page.click_button_order_feed()
        time.sleep(5)
        assert feed_page.availability_modal_window_with_order_details

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_orders_from_order_history_displayed_order_feed(self, driver,auth_user):
        home_page = HomePage(driver)
        time.sleep(5)
        home_page.placing_order()
        home_page.click_button_personal_account()
        account = PersonalAccountPage(driver)
        account.click_button_order_history()
        feed_page = FeedPage(driver)
