from selenium.webdriver.common.by import By


class BasePageLocators:
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
    BUTTON_ORDER_FEED = (By.XPATH, "//p[text()='Лента Заказов']")
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")

    MODAL_WINDOW_TO_CLOSE=(By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")