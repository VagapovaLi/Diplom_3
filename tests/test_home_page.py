import allure
import pytest
import time
import urls
#from pages.feed_page import FeedPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.home_page
@allure.feature(' "Главная" cтраница')
class TestHomePage:
    @allure.title('Проверка перехода на главную страницу "Конструктор"')
    def test_go_to_constructor(self, driver):
        home_page = HomePage(driver)
        home_page.open(urls.LOGIN_URL,wait_seconds=3)
        home_page.click_button_link_constructor()
        current_url = home_page.find_home_page_title_and_return_current_url()
        assert current_url == urls.BASE_URL

    @allure.title('Проверка перехода в "Лента заказов"')
    def test_go_to_constructor(self, driver):
        home_page = HomePage(driver)
        home_page.open(urls.LOGIN_URL,wait_seconds=3)
        home_page.click_button_order_feed()
        current_url = home_page.transition_order_feed_and_return_current_url()
        assert current_url == urls.FEED_URL

    @allure.title('При клике на ингредиент, появляется всплывающее окно с деталями')
    def test_click_ingredient_open_window_with_details(self, driver):
        home_page = HomePage(driver)
        home_page.open(urls.BASE_URL,wait_seconds=3)
        home_page.click_ingredient()
        expected_text = 'Детали ингредиента'
        actual_text = home_page.availability_modal_window_ingredient_details_text()
        assert actual_text == expected_text

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_click_ingredient_open_window_with_details(self, driver):
        home_page = HomePage(driver)
        home_page.open(urls.BASE_URL,wait_seconds=3)
        home_page.click_ingredient()
        home_page.click_close_modal()
        assert home_page.control_close_modal_window()

    #тут именно в мазиле не перетаскивается соус
    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_click_ingredient_open_window_with_details(self, driver):
        home_page = HomePage(driver)
        home_page.open(urls.BASE_URL,wait_seconds=3)
        home_page.add_sauce_basket()
        time.sleep(5)
        first_addition = home_page.get_count_ingredients_in_basket()
        home_page.add_sauce_basket()
        time.sleep(5)
        second_addition = home_page.get_count_ingredients_in_basket()
        time.sleep(5)
        print(second_addition)
        assert second_addition > first_addition


    @allure.title('Авторизованный пользователь оформил заказ')
    def test_authorized_user_placed_order(self, driver, auth_user):
        home_page = HomePage(driver)
        home_page.add_sauce_basket()
        home_page.click_button_place_order()
        actual_message = home_page.availability_modal_window_ingredient_details_text()
        expected_message = 'Ваш заказ начали готовить'
        assert actual_message == expected_message

