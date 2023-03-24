from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time


def isBasketEmptyStatusTextPresent(driver):
    try:
        time.sleep(2)
        driver.find_element(By.XPATH, "//h4[@class='cart-dummy__heading']")
        time.sleep(2)
    except NoSuchElementException:
        time.sleep(2)
        return False
    return True


def getGoodsInCartListSize(driver):
    goods_in_cart_title_price = []
    for elem in driver.find_elements(By.XPATH, "//p[@data-testid='cost']"):
        goods_in_cart_title_price.append(elem.text)
    return goods_in_cart_title_price.__len__()
