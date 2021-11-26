import time
from selenium.webdriver.common.by import By


def test_button_add_to_basket_is_present(browser):
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    time.sleep(30)
    assert button.is_displayed() is True
