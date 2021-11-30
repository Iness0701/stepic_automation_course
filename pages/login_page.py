from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        actual_url = self.browser.current_url
        assert "login" in actual_url
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_address_field = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS)
        email_address_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password_field.send_keys(password)
        repeat_password_field = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD)
        repeat_password_field.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

