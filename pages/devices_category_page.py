from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time
import re


def getSmartphonePriceText(driver, index):
    driver.execute_script("window.scrollTo(0, 220)")
    xpath = f"//span[@class='goods-tile__price-value'][{index}]"
    return int(re.sub('\D', '', driver.find_element(By.XPATH, xpath).text))


def get_goods_title_text_by_index(driver, index):
    xpath = f"//span[@class='goods-tile__title'][{index}]"
    goods_title_text = driver.find_element(By.XPATH, xpath).text
    return goods_title_text


def clickBuyButtonByIndex(self, driver, index):
    driver.execute_script("window.scrollTo(0, 250)")
    time.sleep(2)
    element = driver.find_element(By.XPATH, f"//button[contains(@class,'buy-button')][{index}]")
    element.click()


def get_goods_description_text_by_index(driver, index):
    xpath = f"//a[@data-testid='title'][{index}]"
    goods_title_text = driver.find_element(By.XPATH, xpath).text
    return goods_title_text


def clickOnShoppingBasketButton(driver):
    shopping_basket_button = driver.find_element(By.XPATH,
                                                 "//li[contains(@class,'cart')]/*/button[contains(@class,'header__button')]")
    shopping_basket_button.click()
    time.sleep(3)
