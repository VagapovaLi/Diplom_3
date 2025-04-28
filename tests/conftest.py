import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@allure.step('Открытие браузер')
@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    driver = None
    if request.param == 'chrome':
        chrome_options = ChromeOptions()
        #chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(1920, 1080)
    elif request.param == 'firefox':
        firefox_options = FirefoxOptions()
        #firefox_options.add_argument('--headless')
        driver = webdriver.Firefox(options=firefox_options)
        driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()