import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en, ru, etc.")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print(f"\nstart browser for test.. Language={language}")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()
