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
        home_page.placing_order()
        time.sleep(5)
        home_page.click_button_personal_account()
        account = PersonalAccountPage(driver)
        account.click_button_order_history()
        last_order_number_in_account = account.get_last_order_data()
        feed_page = FeedPage(driver)
        assert feed_page.find_target_order_in_history(last_order_number_in_account)

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_creating_new_order_completed_all_time_counter_increases(self, driver,auth_user):
        home_page = HomePage(driver)
        time.sleep(3)
        home_page.click_button_order_feed()
        feed_page = FeedPage(driver)
        total_old_value =feed_page.get_number_completed_orders_all_time()
        feed_page.click_button_link_constructor()
        home_page = HomePage(driver)
        home_page.placing_order()
        home_page.click_button_order_feed()
        new_value =feed_page.get_number_completed_orders_for_today()
        assert new_value > total_old_value

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_creating_new_order_completed_today_counter_increases(self, driver,auth_user):
        home_page = HomePage(driver)
        time.sleep(3)
        home_page.click_button_order_feed()
        feed_page = FeedPage(driver)
        all_orders_today =feed_page.get_number_completed_orders_all_time()
        feed_page.click_button_link_constructor()
        home_page = HomePage(driver)
        home_page.placing_order()
        home_page.click_button_order_feed()
        new_value_orders_today =feed_page.get_number_completed_orders_for_today()
        assert new_value_orders_today > all_orders_today

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_after_placing_order_number_appears_in_the_progress_section(self, driver,auth_user):
        home_page = HomePage(driver)
        time.sleep(3)
        order_id = home_page.placing_order()
        time.sleep(10)
        home_page.click_button_order_feed()
        time.sleep(3)
        feed_page = FeedPage(driver)
        time.sleep(3)
        assert feed_page.get_order_in_progress_list(order_id)