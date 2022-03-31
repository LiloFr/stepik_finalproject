import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action = 'store', default = "en",
                     help = 'Write a language: es, ru or fr')


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    browser_user_lang = request.config.getoption("language")
    options.add_experimental_option('prefs', {"intl.accept_languages": browser_user_lang})
    browser = webdriver.Chrome(options = options)
    yield browser
    print("\nquit browser..")
    browser.quit()