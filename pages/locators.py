from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    GO_TO_BASKET_BUTTON = (By.XPATH, "//a[text()='View basket']")

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

# class MainPageLocators():
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    EMAIL_ADDRESS = (By.NAME, "registration-email")

    PASSWORD = (By.NAME, "registration-password1")

    REPEAT_PASSWORD = (By.NAME, "registration-password2")

    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")

    # ALERT_ITEM_ADDED_TO_BASKET = (By.XPATH, "//div[contains(text(), 'has been added to your basket')]")
    ALERT_ITEM_ADDED_TO_BASKET = (By.CSS_SELECTOR, ".alertinner")

    ALERT_PRICE = (By.XPATH, "//p[contains(text(), 'Your basket total is now')]")

    PRODUCT_TITLE = (By.TAG_NAME, "h1")

    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")

class BasketPageLocators():
    BASKET_HEADER = (By.TAG_NAME, "h1")

    BASKET_IS_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner")

    ITEM_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")


