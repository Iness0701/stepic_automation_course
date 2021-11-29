import math

from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):
    def click_add_to_basket_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def get_product_title(self):
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        return product_title

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price

    def make_sure_item_is_added_to_basket(self):
        alert_text = self.browser.find_element(*ProductPageLocators.ALERT_ITEM_ADDED_TO_BASKET).text
        product_text = self.get_product_title()
        assert product_text in alert_text
        assert "book" not in alert_text

    def make_sure_price_is_correct(self):
        alert_text = self.browser.find_element(*ProductPageLocators.ALERT_PRICE).text
        product_price = self.get_product_price()
        assert product_price in alert_text



