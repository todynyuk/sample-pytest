from selenium.webdriver.common.by import By
import time
import re


def verify_device_short_characteristic(driver, param):
    short_characteristic = driver.find_element(By.XPATH, "//h1[@class='product__title']").text
    return short_characteristic.__contains__(str(param))


def get_device_short_characteristic(driver):
    return driver.find_element(By.XPATH, "//h1[@class='product__title']").text


def get_chosen_product_price(driver):
    time.sleep(3)
    chosen_product_price = re.sub('\D', '', driver.find_element(By.XPATH,
                                                                "//p[contains(@class,'product-price__big')]").text)
    return chosen_product_price
