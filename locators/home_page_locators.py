from selenium.webdriver.common.by import By


class HomePageLocators:
    MODAL_ASSEMBLE_BURGER = (By.XPATH, "//h1[text()='Соберите бургер']")
    FIRST_BUN_INGREDIENT = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    LABEL_MODAL_WINDOW = (By.XPATH, "//h2[text()='Детали ингредиента']")