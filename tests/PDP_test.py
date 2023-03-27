import logging

from pytest_zebrunner import attach_test_run_label, attach_test_run_artifact_reference, attach_test_label, \
    attach_test_screenshot
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler
from pytest_zebrunner import CurrentTestRun

from pages.device_page import verify_device_short_characteristic, get_chosen_product_price
from pages.devices_category_page import choose_ram_сapacity, click_check_box_filter, getSmartphonePriceText, \
    clickLinkMoreAboutDevice
from pages.main_page import click_universal_category_link
from pages.subcategory_page import click_universal_subcategory_menu_link
from utils.attachments import attach_screenshot

logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)

attach_test_run_label("TestRunLabelRunName", "PyTest")
attach_test_run_label("TestRunLabelResourceName", "Rozetka")

attach_test_run_artifact_reference("Rozetka", "https://rozetka.com.ua/ua/")

CurrentTestRun.set_locale("en_US")
CurrentTestRun.set_build("TR build version")
url = "https://rozetka.com.ua/ua/"


def testItemRamAndPrice(driver):
    logger.info("Attaching labels, artifacts and artifacts references to test")
    attach_test_label("TestLabel", "Rozetka")
    attach_test_run_artifact_reference("Rozetka", "https://rozetka.com.ua/ua/")
    logger.info("Navigating to url: " + url)
    driver.get(url=url)
    attach_screenshot(driver)
    click_universal_category_link(driver, "Смартфони")
    attach_screenshot(driver)
    click_universal_subcategory_menu_link("Мобільні", driver)
    attach_screenshot(driver)
    choose_ram_сapacity(driver, 12)
    attach_screenshot(driver)
    click_check_box_filter(driver, "Синій")
    attach_screenshot(driver)
    smartphone_price = getSmartphonePriceText(driver, 1)
    clickLinkMoreAboutDevice(driver, 1)
    attach_screenshot(driver)
    short_characteristics = verify_device_short_characteristic(driver, 12)
    attach_screenshot(driver)
    chosen_device_price = get_chosen_product_price(driver)
    assert short_characteristics, "Short_characteristics don't contains chosen ram capacity"
    assert str(smartphone_price) == chosen_device_price, "Prices are not equals"
