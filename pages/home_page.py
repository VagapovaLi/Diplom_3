import allure
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Проверяем переход на главную страницу')
    def find_home_page_title_and_return_current_url(self):
        self.find_visibility_element(*HomePageLocators.MODAL_ASSEMBLE_BURGER)
        return self.get_current_url()

    @allure.step('Нажимаем на ингредиент')
    def click_ingredient(self):
        self.find_clickable_element(*HomePageLocators.FIRST_BUN_INGREDIENT).click()

    @allure.step('Проверяем что есть модальное окно "Детали ингредиента"')
    def availability_modal_window_ingredient_details_text(self):
        return self.find_visibility_element(*HomePageLocators.LABEL_MODAL_WINDOW).text

    @allure.step('Закрыть через клик по крестику окно модальное окно')
    def click_close_modal(self):
        self.find_clickable_element(*HomePageLocators.BUTTON_CLOSE_MODAL_DETAIL).click()

    @allure.step('Проверяем, что модальное окно закрыто')
    def control_close_modal_window(self):
        return self.wait_element_disappears(*HomePageLocators.BUTTON_CLOSE_MODAL_DETAIL)

    @allure.step('Нажать на кнопку Оформить заказ')
    def click_order_button(self):
        self.find_clickable_element(*HomePageLocators.BUTTON_PLACE_ORDER).click()

    @allure.step('Ждем полного формирования модального окна заказа')
    def wait_order_modal_loaded(self):
        self.wait_element_disappears(*HomePageLocators.LOADING_MODAL_WINDOW_ORDER)

    @allure.step('Добавляем булочку в корзину')
    def add_sauce_basket_test(self):
        self.drag_and_drop(*HomePageLocators.IMG_BUN_INGREDIENT)

    @allure.step('Получаем каунтер для соуса')
    def get_count_ingredients_in_basket(self):
        self.presence_of_elements(*HomePageLocators.SAUCE_COUNTER)
        element = self.driver.find_element(*HomePageLocators.SAUCE_COUNTER)
        count_text = element.text
        count = int(count_text) if count_text.isdigit() else 0
        return count

    @allure.step('Нажимаем на кнопку "Оформить заказ"')
    def click_button_place_order(self):
        self.find_clickable_element(*HomePageLocators.BUTTON_PLACE_ORDER).click()

    @allure.step('Проверяем что есть модальное окно "Ваш заказ начали готовить"')
    def availability_modal_window_order_has_started_text(self):
        return self.find_visibility_element(*HomePageLocators.ORDER_CONFIRMATION_WINDOW).text

    @allure.step('Получаем идентификатор заказа')
    def get_order_id(self):
        return self.find_visibility_element(*HomePageLocators.BUTTON_CROSS_MODAL_ORDER).text

    @allure.step('Получаем номер заказа в работе')
    def get_order_in_work(self):
        return self.find_visibility_element(*HomePageLocators.NUMBER_IN_WORK).text

    @allure.step('Добавить ингредиент')
    def add_filling_to_order(self):
        self.drag_and_drop(*HomePageLocators.IMG_BUN_INGREDIENT, *HomePageLocators.BASKET)

    @allure.step('Добавить соус')
    def add_filling_to_order_sauce(self):
        self.drag_and_drop(*HomePageLocators.IMG_SAUCE_INGREDIENT, *HomePageLocators.BASKET)


    @allure.step('Закрываем модальное окно заказа')
    def click_cross_in_order_modal_window(self):
        self.find_clickable_element(*HomePageLocators.BUTTON_CROSS_MODAL_ORDER).click()


    @allure.step('Сделать заказ')
    def make_order(self):
        self.add_filling_to_order()
        self.click_button_place_order()
        self.wait_order_modal_loaded()
        order_id = self.get_order_id()
        self.click_cross_in_order_modal_window()
        return order_id

    @allure.step('Сделать заказ sauce')
    def make_order_sauce(self):
        self.add_filling_to_order_sauce()
        self.click_button_place_order()
        self.wait_order_modal_loaded()
        order_id = self.get_order_id()
        self.click_cross_in_order_modal_window()
        return order_id


