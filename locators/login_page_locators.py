from selenium.webdriver.common.by import By


class LoginPageLocators:
    BUTTON_RECOVER_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")                                 # кнопка Восстоновить пароль

    INPUT_EMAIL = (By.XPATH, "//input[@type='text']")
    INPUT_PASSWORD = (By.XPATH, "//input[@type='password']")
    BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти']")