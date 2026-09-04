from selenium.webdriver.common.by import By


class HomePage:

    FIRST_PRODUCT = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self):
        self.driver.find_element(*self.FIRST_PRODUCT).click()

    def open_cart(self):
        self.driver.find_element(*self.CART_BUTTON).click()

    def logout(self):
        self.driver.find_element(*self.MENU_BUTTON).click()
        self.driver.find_element(*self.LOGOUT_LINK).click()
