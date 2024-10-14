from selene import browser
import pytest


@pytest.fixture(scope='session', autouse=True)
def open_browser():
    browser.open('https://ru.wikipedia.org')
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    yield
    browser.quit()
