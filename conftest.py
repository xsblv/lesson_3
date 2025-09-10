from selene import browser, be, have
import pytest

@pytest.fixture()
def browser_size():
    browser.config.window_width = 360
    browser.config.window_height = 712

@pytest.fixture()
def open_browser(browser_size):
    browser.open('https://www.drive2.ru/')

    yield browser
    browser.quit()