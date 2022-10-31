import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Select the language in which the website will be displayed.")


@pytest.fixture(scope="session")
def browser_language(request):
    return request.config.getoption("language")


@pytest.fixture(scope="function")
def browser(browser_language):
    if browser_language:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be 'ar', 'ca', 'cs', 'da', 'de', 'en-gb', 'el', 'es', 'fi', 'fr',\
'it', 'ko', 'nl', 'pl', 'pt', 'pt-br', 'ro', 'ru', 'sk', 'uk', 'zh-hans'")
    yield browser
    print("\nquit browser..")
    browser.quit()
