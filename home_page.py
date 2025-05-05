import allure
import time
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
        WebDriverWait(self.driver, 20).until(
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
        try:
            close_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(HomePageLocators.BUTTON_CLOSE_MODAL_DETAIL)
            )
            close_button.click()

            # Ожидаем исчезновения модального окна
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located(HomePageLocators.MODAL_WINDOW_LOCATOR)
                # Замените на актуальный локатор модального окна
            )
        except TimeoutException:
            print("Модальное окно не закрылось вовремя.")

    @allure.step('Проверяем, что модальное окно закрыто')
    def control_close_modal_window(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located(HomePageLocators.BUTTON_CLOSE_MODAL_DETAIL)
            )
            return True
        except TimeoutException:
            return False

    @allure.step('Добавить ингредиент')
    def add_filling_to_order(self):

        self.drag_and_drop(*HomePageLocators.IMG_BUN_INGREDIENT, *HomePageLocators.BASKET)




    @allure.step('Нажать на кнопку Оформить заказ')
    def click_order_button(self):
        self.find_clickable_element(*HomePageLocators.BUTTON_PLACE_ORDER).click()

    @allure.step('Ждем полного формирования модального окна заказа')
    def wait_order_modal_loaded(self):
        self.wait_element_disappears(*HomePageLocators.LOADING_MODAL_WINDOW_ORDER)

    @allure.step('Добавляем булочку в корзину')
    def add_bun_basket(self):
        bun = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable( HomePageLocators.IMG_BUN_INGREDIENT)
        )
        target = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located( HomePageLocators.BASKET)
        )
        actions = ActionChains(self.driver)
        time.sleep(5)
        actions.click_and_hold(bun).move_to_element(target).release().perform()


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
        return self.find_visability_element(*HomePageLocators.ORDER_ID_MODAL_WINDOW).text



    @allure.step('Закрываем модальное окно заказа')
    def click_cross_in_order_modal_window(self):
        cross_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(HomePageLocators.BUTTON_CROSS_MODAL_ORDER)
        )
        cross_button.click()
        #self.find_clickable_element(*HomePageLocators.BUTTON_CROSS_MODAL_ORDER).click()

    @allure.step('Перетаскиваем соус в корзину')
    def add_sauce_basket(self):
        self.drag_and_drop(*HomePageLocators.BUN_INGREDIENT_SAUCE, *HomePageLocators.BASKET)


    @allure.step('Сделать заказ')
    def placing_order(self):

        self.add_filling_to_order()
        self.click_order_button()
        self.wait_order_modal_loaded()
        order_id = self.get_order_id()
        self.click_cross_in_order_modal_window()
        return order_id

    @allure.step('Переместиться к элементу и нажать')
    def click_cross_order(self):
        self.move_to_element_and_click(HomePageLocators.CROSS_ORDER)

    # @allure.step('Оформляем заказ с булочкой')
    # def placing_order_bun(self):
    #     self.add_bun_basket()
    #
    #     self.click_order_button()
    #     order_id = self.get_order_id()
    #     self.click_close_modal()
    #     return order_id


    @allure.step('Получаем номер заказа в работе')
    def get_order_in_work(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(HomePageLocators.NUMBER_IN_WORK))
        return self.get_text(HomePageLocators.NUMBER_IN_WORK)