import logging
import time

from pytest_zebrunner import attach_test_run_label, attach_test_run_artifact_reference, attach_test_label, \
    attach_test_screenshot
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler
from pytest_zebrunner import CurrentTestRun
from selenium.webdriver.common.by import By

from pages.shopping_basket_page import isBasketEmptyStatusTextPresent, getGoodsInCartListSize

logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)

attach_test_run_label("TestRunLabelRunName", "PyTest")
attach_test_run_label("TestRunLabelResourceName", "Rozetka")

attach_test_run_artifact_reference("Rozetka", "https://rozetka.com.ua/ua/")

CurrentTestRun.set_locale("en_US")
CurrentTestRun.set_build("TR build version")

url = "https://rozetka.com.ua/ua/"


def testAddGoodsInBasketAndCheckItEmpty(driver):
    logger.info("Attaching labels, artifacts and artifacts references to test")
    attach_test_label("TestLabel", "Rozetka")
    attach_test_run_artifact_reference("Rozetka", "https://rozetka.com.ua/ua/")
    logger.info("Navigating to url: " + url)
    driver.get(url=url)
    attach_screenshot(driver)
    driver.find_element(By.XPATH, f"//a[@class='menu-categories__link' and contains(.,'{'Смартфони'}')]").click()
    attach_screenshot(driver)
    driver.find_element(By.XPATH,
                        f"//a[contains(@class,'tile-cats__heading') and contains(.,'{'Мобільні'}')]").click()
    attach_screenshot(driver)
    driver.execute_script("window.scrollTo(0, 250)")
    time.sleep(2)
    element = driver.find_element(By.XPATH, f"//button[contains(@class,'buy-button')][{1}]")
    element.click()
    time.sleep(3)
    attach_screenshot(driver)
    driver.find_element(By.XPATH, "//li[contains(@class,'cart')]/*/button[contains(@class,'header__button')]").click()
    attach_screenshot(driver)
    assert isBasketEmptyStatusTextPresent(driver) == False, \
        "Basket empty status text is presented"
    goods_in_shopping_basket_count = getGoodsInCartListSize(driver)
    assert goods_in_shopping_basket_count > 0, "Basket is empty"
    logger.info("'testAddGoodsInBasketAndCheckItEmpty' was successfully finished")


def attach_screenshot(driver):
    driver.save_screenshot("screenshot.png")
    attach_test_screenshot("screenshot.png")
