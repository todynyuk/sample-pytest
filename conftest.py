import os

import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    zebrunner_selenium_grid = os.getenv("ZEBRUNNER_SELENIUM_GRID", "http://127.0.0.1:4444")
    # zebrunner_selenium_grid = os.getenv("ZEBRUNNER_SELENIUM_GRID", "https://solvdinternal:O9JjPcqxJ0hPs685@engine.zebrunner.com/wd/hub")


    # options = webdriver.ChromeOptions()
    # options.platform_name = "linux"
    # options.browser_version = "latest"
    options = webdriver.FirefoxOptions()
    options.platform_name = "linux"
    # options.browser_version = "108.0"
    options.browser_version = "latest"
    options.set_capability("enableVideo", "true")

    driver = webdriver.Remote(
        command_executor=zebrunner_selenium_grid,
        options=options
    )

    driver.implicitly_wait(10)
    driver.maximize_window()

    yield driver

    driver.quit()

