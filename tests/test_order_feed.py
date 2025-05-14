import allure
import pytest
import urls
from pages.feed_page import FeedPage
from pages.home_page import HomePage
from pages.personal_account_page import PersonalAccountPage


@pytest.mark.feed_page
@allure.feature('Страница "Лента заказов"')
class TestFeedOrders:
    @allure.title('Авторизованный пользователь оформил заказ')
    def test_authorized_user_placed_order(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open(urls.FEED_URL)
        feed_page.click_button_order_feed()
        assert feed_page.availability_modal_window_with_order_details

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_orders_from_order_history_displayed_order_feed(self, driver,auth_user):
        home_page = HomePage(driver)
        home_page.make_order_sauce()
        home_page.click_button_personal_account()
        account = PersonalAccountPage(driver)
        account.click_button_order_history()
        last_order_number_in_account = account.get_last_order_data()
        feed_page = FeedPage(driver)
        assert feed_page.find_target_order_in_history(last_order_number_in_account)

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_creating_new_order_completed_all_time_counter_increases(self, driver,auth_user):
        feed_page = FeedPage(driver)
        feed_page.click_button_order_feed()
        total_old_value = feed_page.get_number_completed_orders_all_time()
        feed_page.click_button_link_constructor()
        home_page = HomePage(driver)
        home_page.make_order_sauce()
        home_page.click_button_order_feed()
        new_value =feed_page.get_number_completed_orders_all_time()
        assert int(new_value) > int(total_old_value)

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_creating_new_order_completed_today_counter_increases(self, driver,auth_user):
        feed_page = FeedPage(driver)
        feed_page.click_button_order_feed()
        all_orders_today =feed_page.get_number_completed_orders_for_today()
        feed_page.click_button_link_constructor()
        home_page = HomePage(driver)
        home_page.make_order_sauce()
        home_page.click_button_order_feed()
        new_value_orders_today =feed_page.get_number_completed_orders_for_today()
        assert int(new_value_orders_today)  > int(all_orders_today)

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_after_placing_order_number_appears_in_the_progress_section(self, driver,auth_user):
        home_page = HomePage(driver)
        order_id = home_page.make_order_sauce()
        home_page.click_button_order_feed()
        feed_page = FeedPage(driver)
        assert feed_page.get_order_in_progress_list(order_id)


