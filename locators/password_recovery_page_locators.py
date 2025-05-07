from selenium.webdriver.common.by import By

class PasswordRecoveryPageLocators:
    EMAIL_INPUT = (By.XPATH, '//input[@name="name"]')                                                                   #поле ввода email
    BUTTON_RECOVER = (By.XPATH, '//button[text()="Восстановить"]')                                                      #кнопка «Восстановить» в форме восстановления пароля
    BUTTON_SAVE = (By.XPATH, '//button[text()="Сохранить"]')
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")                                                            #поле ввода пароля
    BUTTON_SHOW_PASSWORD = (By.CSS_SELECTOR, '.input__icon')
    ACTIVE_INPUT_PASSWORD = (By.CSS_SELECTOR, '.input_status_active')