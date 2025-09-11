
from selene import browser, be, have
import pytest

@pytest.fixture()
def browser_size():
    browser.config.window_width = 1200
    browser.config.window_height = 800


@pytest.fixture()
def open_browser(browser_size):
    browser.open('https://www.drive2.ru/')
    #assert browser.config.window_width == 1200, "Ширина окна не соответствует заданному значению"
    #assert browser.config.window_height == 800, "Высота окна не соответствует заданному значению"
    yield browser
    browser.quit()

