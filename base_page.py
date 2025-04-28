
import allure





class BasePage:
    def __init__(self, driver):
        self.driver = driver


    @allure.step('Открываем страницу: {url}')
    def open(self, url):
        self.driver.get(url)