import sys
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Config
from utils.driver_factory import create_driver
from pages.login_page import LoginPage
from pages.home_page import HomePage


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_login_and_workflow():

    driver = create_driver()

    try:
        # Step 1: Open application
        login_page = LoginPage(driver)
        login_page.open(Config.BASE_URL)
        time.sleep(2)  # Wait for the page to load

        # Step 2: Login
        login_page.login("standard_user", "secret_sauce")
        time.sleep(2)  # Wait for the login to complete

        # Step 3: Create home page object
        home_page = HomePage(driver)
        time.sleep(2)  # Wait for the home page to load

        # Step 4: Add product
        home_page.add_product_to_cart()
        time.sleep(2)  # Wait for the product to be added to the cart

        # Step 5: Open cart
        home_page.open_cart()
        time.sleep(2)  # Wait for the cart page to load

        # Step 6: Validate cart
        cart_item = driver.find_element(
            By.CLASS_NAME,
            "inventory_item_name"
        )
        
        assert cart_item.text == "Sauce Labs Backpack"
        time.sleep(2)  # Wait for the cart item to be visible
 
        # Step 7: Logout
        #1 open the sidebar menu 
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        #2 wait for the logout link to be clickable
        wait = WebDriverWait(driver, 10)
        logout_btn = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        logout_btn.click()
        #home_page.logout()
        time.sleep(2)  # Wait for the logout to complete    
    finally:
        driver.quit()
