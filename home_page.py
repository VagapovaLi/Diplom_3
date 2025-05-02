import allure

from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.feed_page_locators import FeedPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

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

    @allure.step('Закрыть через клик по крестику окно модальное окно')
    def click_close_modal(self):
        WebDriverWait(self.driver,  10).until(
            EC.element_to_be_clickable(HomePageLocators.BUTTON_CLOSE_MODAL_DETAIL)
        ).click()

    @allure.step('Проверяем, что модальное окно закрыто')
    def control_close_modal_window(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located(HomePageLocators.BUTTON_CLOSE_MODAL_DETAIL)
            )
            return True
        except TimeoutException:
            return False

    @allure.step('Добавляем соус в корзину')
    def add_sauce_basket(self):
        source = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable( HomePageLocators.BUN_INGREDIENT)
        )
        target = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located( HomePageLocators.BASKET)
        )
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()



    @allure.step('Получаем каунтер для соуса')
    def get_count_ingredients_in_basket(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located( HomePageLocators.SAUCE_COUNTER)
        )
        element = self.driver.find_element(*HomePageLocators.SAUCE_COUNTER)
        count_text = element.text  # Получаем текст из элемента
        count = int(count_text) if count_text.isdigit() else 0  # Преобразуем в целое число

        return count


    @allure.step('Нажимаем на кнопку "Оформить заказ"')
    def click_button_place_order(self):
        WebDriverWait(self.driver,  10).until(
            EC.element_to_be_clickable(HomePageLocators.BUTTON_PLACE_ORDER)
        ).click()


    @allure.step('Проверяем что есть модальное окно "Ваш заказ начали готовить"')
    def availability_modal_window_ingredient_details_text(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(HomePageLocators.ORDER_CONFIRMATION_WINDOW)
        )
        return element.text


    @allure.step('Получаем Id заказа')
    def get_order_id(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(HomePageLocators.WINDOW_WITH_ORDER_ID)
        )
        return element.text


    @allure.step('Оформляем заказ')
    def placing_order(self):
        self.add_sauce_basket()
        self.click_button_place_order()
        order_id = self.get_order_id()
        self.click_close_modal()
        return order_id