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


def verifyChosenParameterInShortCharacteristics(driver, param):
    time.sleep(3)
    driver.execute_script("arguments[0].scrollIntoView();",
                          driver.find_element(By.XPATH, "//p[@class='product-about__brief ng-star-inserted']"))
    short_characteristic = driver.find_element(By.XPATH, "//p[@class='product-about__brief ng-star-inserted']").text
    return short_characteristic.__contains__(str(param))


def verifyChosenParamInAllCharacteristics(driver, param):
    short_characteristic = driver.find_element(By.XPATH,
                                               "//h3[@class='product-tabs__heading']//span[contains(@class,'heading_color_gray')]").text
    return short_characteristic.__contains__(str(param))
