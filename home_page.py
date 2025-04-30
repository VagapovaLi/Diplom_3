import allure

from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.feed_page_locators import FeedPageLocators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)



    @allure.step('Проверяем переход на главную страницу')
    def find_home_page_title_and_return_current_url(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(HomePageLocators.MODAL_ASSEMBLE_BURGER)
        )
        return self.driver.current_url


    @allure.step('Проверяем переход в "Лента заказов"')
    def transition_order_feed_and_return_current_url(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(FeedPageLocators.MODAL_ORDER_FEED)
        )
        return self.driver.current_url


    @allure.step('Нажимаем на ингредиент')
    def click_ingredient(self):
        WebDriverWait(self.driver,  10).until(
            EC.element_to_be_clickable(HomePageLocators.FIRST_BUN_INGREDIENT)
        ).click()

    @allure.step('Проверяем что есть модальное окно "Детали ингредиента"')
    def availability_modal_window_ingredient_details_text(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(HomePageLocators.LABEL_MODAL_WINDOW )
        )
        return element.text