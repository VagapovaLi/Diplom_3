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

    @allure.step('Добавить соус')
    def add_filling_to_order_sauce(self):
        source = self.get_element(HomePageLocators.IMG_SAUCE_INGREDIENT)
        target = self.get_element(HomePageLocators.BASKET)
        self.drag_and_drop(source, target)

    @allure.step('Добавить ингредиент в корзину')
    def add_ingredient_in_basket(self):
        element = self.get_element(HomePageLocators.IMG_SAUCE_INGREDIENT)
        target = self.get_element(HomePageLocators.BASKET_AREA)
        self.drag_and_drop(element, target)
        element_1 = self.get_element(HomePageLocators.FIRST_BUN_INGREDIENT)
        target_1 = self.get_element(HomePageLocators.BASKET_AREA)
        self.drag_and_drop(element_1, target_1)

    @allure.step('Сделать заказ')
    def make_order_sauce(self):
        self.add_ingredient_in_basket()
        self.click_button_place_order()
        self.wait_for_text_to_disappear(HomePageLocators.ORDER_NUMBER, "9999")
        order = self.get_text(*HomePageLocators.ORDER_NUMBER)
        button = self.driver.find_element(*HomePageLocators.BUTTON_CROSS_MODAL_ORDER)
        self.driver.execute_script("arguments[0].click();", button)
        return order
