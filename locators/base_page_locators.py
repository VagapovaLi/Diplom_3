from selenium.webdriver.common.by import By

class BasePageLocators:
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
    BUTTON_ORDER_FEED =  (By.XPATH, "// a[ @ href = '/feed']")
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")
