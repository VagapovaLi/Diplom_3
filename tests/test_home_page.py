import allure
import pytest
import urls
from pages.home_page import HomePage
from pages.feed_page import FeedPage

@pytest.mark.home_page
@allure.feature(' "Главная" cтраница')
class TestHomePage:
    @allure.title('Проверка перехода на главную страницу "Конструктор"')
    def test_go_to_constructor(self, driver):
        home_page = HomePage(driver)
        home_page.open(urls.LOGIN_URL)
        home_page.click_button_link_constructor()
        current_url = home_page.find_home_page_title_and_return_current_url()
        assert current_url == urls.BASE_URL

    @allure.title('Проверка перехода в "Лента заказов"')
    def test_go_to_order_feed(self, driver):
        home_page = HomePage(driver)
        home_page.open(urls.LOGIN_URL)
        home_page.click_button_order_feed()
        feed_page = FeedPage(driver)
        current_url = feed_page.transition_order_feed_and_return_current_url()
        assert current_url == urls.FEED_URL

    @allure.title('При клике на ингредиент, появляется всплывающее окно с деталями')
    def test_click_ingredient_open_window_with_details(self, driver):
        home_page = HomePage(driver)
        home_page.open(urls.BASE_URL)
        home_page.click_ingredient()
        expected_text = 'Детали ингредиента'
        actual_text = home_page.availability_modal_window_ingredient_details_text()
        assert actual_text == expected_text

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_pop_up_window_closed_clicking_cross(self, driver):
        home_page = HomePage(driver)
        home_page.open(urls.BASE_URL)
        home_page.click_ingredient()
        home_page.click_close_modal()
        assert home_page.control_close_modal_window()

    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_add_ingredient_order_counter_ingredient_increases(self, driver):
        home_page = HomePage(driver)
        home_page.open(urls.BASE_URL)
        home_page.add_filling_to_order_sauce()
        first_addition = home_page.get_count_ingredients_in_basket()
        home_page.add_filling_to_order_sauce()
        second_addition = home_page.get_count_ingredients_in_basket()
        assert second_addition > first_addition


    @allure.title('Авторизованный пользователь оформил заказ')
    def test_authorized_user_placed_order(self, driver, auth_user):
        home_page = HomePage(driver)
        home_page.add_filling_to_order_sauce()
        #home_page.make_order()
        home_page.click_button_place_order()
        actual_message = home_page.availability_modal_window_order_has_started_text()
        expected_message = 'Ваш заказ начали готовить'
        assert actual_message == expected_message

