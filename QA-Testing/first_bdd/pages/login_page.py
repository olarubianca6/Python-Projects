from selenium.webdriver.common.by import By

from base_page import BasePage


class LoginPage(BasePage):

    LOGIN_PAGE_URL = "https://demo.nopcommerce.com/login"
    INPUT_EMAIL = (By.ID, "Email")
    INPUT_PASSWORD = (By.ID, "Password")
    BUTTON_LOGIN = (By.CLASS_NAME, "login-button")
    ERROR_MESSAGE = (By.CLASS_NAME, "message-error")

    def open(self):
        self.driver.get(self.LOGIN_PAGE_URL)

    def set_email(self, text):
        self.type(self.INPUT_EMAIL, text)

    def set_password(self, text):
        self.type(self.INPUT_PASSWORD, text)

    def click_login_button(self):
        self.find(self.BUTTON_LOGIN).click()

    def is_main_error_msg_displayed(self):
        return self.find(self.ERROR_MESSAGE).is_displayed()

    def main_error_msg_contains_text(self, text):
        return text in self.get_text(self.ERROR_MESSAGE)
