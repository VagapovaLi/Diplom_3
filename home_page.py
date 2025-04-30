import allure

from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)



    @allure.step('Проверяем переход на главную страницу')
    def find_home_page_title_and_return_current_url(self):

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(HomePageLocators.MODAL_ASSEMBLE_BURGER)
        )
        return self.driver.current_url


