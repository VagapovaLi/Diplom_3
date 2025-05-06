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
        self.find_clickable_element(*FeedPageLocators.FIRST_POSITION_ORDER).click()
        # WebDriverWait(self.driver,  10).until(
        #     EC.element_to_be_clickable(FeedPageLocators.FIRST_POSITION_ORDER)
        # ).click()


    @allure.step('Проверяем что есть модальное окно с  деталями заказа')
    def availability_modal_window_with_order_details(self):
        return self.find_visibility_element(*FeedPageLocators.ORDER_DETAILS_WINDOW).is_displayed()

        # WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located(FeedPageLocators.ORDER_DETAILS_WINDOW)
        # )


    @allure.step('Просматриваем заказы и проверяем наличие созданного')
    def find_target_order_in_history(self, target_order):
        orders = self.presence_of_elements(*FeedPageLocators.LAST_ORDERS)
        return any(target_order == order.text for order in orders)

        #
        # orders= WebDriverWait(self.driver, 20).until(
        #     EC.presence_of_all_elements_located(FeedPageLocators.LAST_ORDERS)
        # )
        # return any(target_order == order.text for order in orders)

    @allure.step('Получаем количество выполненных заказов за всё время')
    def get_number_completed_orders_all_time(self):

        return self.find_visibility_element(*FeedPageLocators.NUMBER_OF_COMPLETED_ORDERS_ALL_TIME).text
        # return WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located(FeedPageLocators.NUMBER_OF_COMPLETED_ORDERS_ALL_TIME)
        # ).text

    @allure.step('Получаем количество выполненных заказов за сегодня')
    def get_number_completed_orders_for_today(self):
        return self.find_visibility_element(*FeedPageLocators.NUMBER_OF_COMPLETED_ORDERS_FOR_TODAY).text
        # return WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located(FeedPageLocators.NUMBER_OF_COMPLETED_ORDERS_FOR_TODAY)
        # ).text

    @allure.step('Проверяем наличие заказа в списке "В работе"')
    def get_order_in_progress_list(self, order_id):

        return self.text_present_in_element(*FeedPageLocators.ORDERS_IN_PROGRESS, order_id)
