from selenium.webdriver.common.by import By
import time


def click_universal_subcategory_menu_link(sub_category, driver):
    time.sleep(10)
    driver.find_element(By.XPATH,
                        f"//a[contains(@class,'tile-cats__heading') and contains(.,'{sub_category}')]").click()
    time.sleep(3)
