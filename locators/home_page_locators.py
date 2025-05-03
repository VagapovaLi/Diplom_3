from selenium.webdriver.common.by import By


class HomePageLocators:
    MODAL_ASSEMBLE_BURGER = (By.XPATH, "//h1[text()='Соберите бургер']")
    FIRST_BUN_INGREDIENT = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    LABEL_MODAL_WINDOW = (By.XPATH, "//h2[text()='Детали ингредиента']")
    BUTTON_CLOSE_MODAL_DETAIL = (By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button")
    BUN_INGREDIENT = (By.XPATH, "//img[@alt='Соус Spicy-X']")
    BASKET = (By.CSS_SELECTOR, '.BurgerConstructor_basket__list__l9dp_')
    SAUCE_COUNTER = (By.XPATH, "//div[2]/ul[2]/a[1]/div[1]/p")
    BUTTON_PLACE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")

    ORDER_CONFIRMATION_WINDOW= (By.CSS_SELECTOR, '.undefined.text.text_type_main-small.mb-2')

    WINDOW_WITH_ORDER_ID=(By.XPATH,"//div/section/div[1]//h2")

    IMG_BUN_INGREDIENT = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    MODAL_WINDOW_LOCATOR = (By.XPATH,'//div/section/div[1]/div')

    ORDER_NUMBER = By.XPATH, '//p[text()="идентификатор заказа"]'

    CROSS_ORDER = By.XPATH, "//button[contains(@class, 'Modal_modal__close')][1]"
    NUMBER_IN_WORK = (By.CSS_SELECTOR, 'ul[class^="OrderFeed_orderListReady"] li[class*="text_type_digits-default"]')