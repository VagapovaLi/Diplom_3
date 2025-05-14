from selenium.webdriver.common.by import By


class FeedPageLocators:

    ORDER_DETAILS_WINDOW= (By.XPATH,"//div/section[2]/div[1]")
    LAST_ORDERS = (By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6']"
                                "//p[@class='text text_type_digits-default']")

    NUMBER_OF_COMPLETED_ORDERS_FOR_TODAY = (By.XPATH, "//div[@class='OrderFeed_ordersData__1L6Iv']"
                              "//div[3]//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']"
                                    "//li[@class='text text_type_digits-default mb-2']")

    MODAL_ORDER_FEED = (By.XPATH, "//p[text()='Лента Заказов']")
    ALL_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
