import os

import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.driver.set_window_size(1920, 1200)
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 4.0

    yield
    browser.quit()

PROJECT_ROOT_PATH = os.path.dirname(__file__)
RESOURCE_PATH = os.path.abspath(os.path.join(PROJECT_ROOT_PATH, 'resource'))