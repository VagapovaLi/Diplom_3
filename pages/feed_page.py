import allure
from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Проверяем что есть модальное окно с  деталями заказа')
    def availability_modal_window_with_order_details(self):
        self.find_visibility_element(*FeedPageLocators.ORDER_DETAILS_WINDOW)

    @allure.step('Просматриваем заказы и проверяем наличие созданного')
    def find_target_order_in_history(self, target_order):
        orders = self.presence_of_elements(*FeedPageLocators.LAST_ORDERS)
        return any(target_order == order.text for order in orders)

    @allure.step('Проверяем переход в "Лента заказов"')
    def transition_order_feed_and_return_current_url(self):
        self.find_visibility_element(*FeedPageLocators.MODAL_ORDER_FEED)
        return self.get_current_url()

    @allure.step('Получаем количество выполненных заказов за всё время')
    def get_number_completed_orders_all_time(self):
        return self.find_visibility_element(*FeedPageLocators.ALL_ORDER_COUNT).text

    @allure.step('Получаем количество выполненных заказов за сегодня')
    def get_number_completed_orders_for_today(self):
        return self.find_visibility_element(*FeedPageLocators.NUMBER_OF_COMPLETED_ORDERS_FOR_TODAY).text


    @allure.step('Проверяем наличие заказа в списке "В работе"')
    def get_order_in_progress_list(self, order_id):
        return self.text_present_in_element(*FeedPageLocators.ORDERS_IN_PROGRESS, order_id)

