from selenium.webdriver.common.by import By


class FeedPageLocators:
    MODAL_ORDER_FEED = (By.XPATH, "//h1[text()='Лента заказов']")
    FIRST_POSITION_ORDER=(By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6' and position()=1]")