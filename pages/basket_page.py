from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_BASKET), \
            "Item in basket is presented, but should not be"

    def text_basket_is_empty(self):
        text = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_TEXT).text
        assert "Your basket is empty." in text, "Basket is not empty, but should be"