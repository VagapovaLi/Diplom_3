import allure
import pytest
import time
import urls
#from pages.feed_page import FeedPage
from pages.home_page import HomePage


@pytest.mark.home_page
@allure.feature(' "Главная" cтраница')
class TestHomePage:
    @allure.title('Проверка перехода на главную страницу "Конструктор"')
    def test_go_to_constructor(self, driver):
        home_page = HomePage(driver)
        home_page.open(urls.LOGIN_URL)
        time.sleep(3)
        home_page.click_button_link_constructor()
        current_url = home_page.find_home_page_title_and_return_current_url()
        assert current_url == urls.BASE_URL

