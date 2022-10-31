from selenium.webdriver.common.by import By
import time


def test_add_to_cart_button_is_displayed(browser, browser_language):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.implicitly_wait(15)
    browser.get(link)
    els = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    time.sleep(10)
    assert len(els), "No element satisfying specified locator"
    assert len(els) == 1, "Element is not unique"
