import allure

from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
class FeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)




    @allure.step('Нажимаем на заказ')
    def click_button_order_feed(self):
        WebDriverWait(self.driver,  10).until(
            EC.element_to_be_clickable(FeedPageLocators.FIRST_POSITION_ORDER)
        ).click()


    @allure.step('Проверяем что есть модальное окно с  деталями заказа')
    def availability_modal_window_with_order_details(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(FeedPageLocators.ORDER_DETAILS_WINDOW)
        )


    @allure.step('Просматриваем заказы и проверяем наличие искомого')
    def find_target_order_in_history(self, target_order):
        orders = self.presence_of_elements(*FeedPageLocators.LAST_50_ORDERS)
        return any(target_order == order.text for order in orders)