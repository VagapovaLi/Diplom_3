
import allure



class BasePage:
    def __init__(self, driver,timeout=20):
        self.driver = driver
        self.timeout = timeout


    @allure.step('Открываем страницу: {url}')
    def open(self, url):
        self.driver.get(url)