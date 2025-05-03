from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
    LABEL_PERSONAL_ACCOUNT = (By.CSS_SELECTOR, '.Account_text__fZAIn')
    BUTTON_ORDER_HISTORY = (By.XPATH, "//a[text()='История заказов']")
    BUTTON_EXIT = (By.XPATH, "//button[text()='Выход']")

    LIST_OF_ORDERS= (By.XPATH, "//div[@class='OrderHistory_orderHistory__qy1VB']"
                                          "//li[position()=last()]//p[@class='text text_type_digits-default']")