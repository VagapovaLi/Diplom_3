from selenium.webdriver.common.by import By


class HomePageLocators:
    MODAL_ASSEMBLE_BURGER = (By.XPATH, "//h1[text()='Соберите бургер']")
    FIRST_BUN_INGREDIENT = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    LABEL_MODAL_WINDOW = (By.XPATH, "//h2[text()='Детали ингредиента']")
    BUTTON_CLOSE_MODAL_DETAIL = (By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button")
    BASKET = (By.CSS_SELECTOR, '.BurgerConstructor_basket__list__l9dp_')
    SAUCE_COUNTER = (By.XPATH, "//div[2]/ul[2]/a[1]/div[1]/p")
    BUTTON_PLACE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")

    ORDER_CONFIRMATION_WINDOW= (By.CSS_SELECTOR, '.undefined.text.text_type_main-small.mb-2')

    IMG_SAUCE_INGREDIENT = (By.XPATH, "//img[@alt='Соус Spicy-X']")
    ORDER_NUMBER = (By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow")]')

    BUTTON_CROSS_MODAL_ORDER = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")

    BASKET_AREA = (By.XPATH, '//ul[contains(@class, "BurgerConstructor_basket")]')
