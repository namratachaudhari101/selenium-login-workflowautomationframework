from selenium import webdriver
from config.config import Config


def create_driver():
    if Config.BROWSER == "chrome":
        driver = webdriver.Chrome()
    else:
        raise ValueError("Unsupported browser")

    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    driver.maximize_window()

    return driver
