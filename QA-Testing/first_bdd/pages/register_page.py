import random
from selenium.webdriver.common.by import By

from base_page import BasePage


class RegisterPage(BasePage):

    INPUT_FIRST_NAME = (By.ID, "FirstName")
    INPUT_LAST_NAME = (By.ID, "LastName")
    INPUT_EMAIL = (By.ID, "Email")
    BUTTON_REGISTER = (By.ID, "register-button")
    SELECT_BIRTH_DAY = (By.NAME, "DateOfBirthDay")
    SELECT_BIRTH_MONTH = (By.NAME, "DateOfBirthMonth")
    SELECT_BIRTH_YEAR = (By.NAME, "DateOfBirthYear")
    INPUT_PASSWORD = (By.ID, "Password")
    INPUT_CONFIRM_PASSWORD = (By.ID, "ConfirmPassword")
    REGISTER_SUCCESS_MESSAGE = (By.CLASS_NAME, "result")

    ERROR_FIRST_NAME = (By.ID, "FirstName-error")
    ERROR_LAST_NAME = (By.ID, "LastName-error")
    ERROR_EMAIL = (By.ID, "Email-error")
    ERROR_PASS = (By.ID, "Password-error")
    ERROR_PASS_CONFIRM = (By.ID, "ConfirmPassword-error")
    
    def open(self):
        self.driver.get("https://demo.nopcommerce.com/register")
        
    def set_first_name(self, first_name):
        self.type(self.INPUT_FIRST_NAME, first_name)
        
    def set_last_name(self, last_name):
        self.type(self.INPUT_LAST_NAME, last_name)
        
    def select_day_of_birth(self, day):
        self.select_by_text(self.SELECT_BIRTH_DAY, day)

    def select_month_of_birth(self, month):
        self.select_by_text(self.SELECT_BIRTH_MONTH, month)

    def select_year_of_birth(self, year):
        self.select_by_text(self.SELECT_BIRTH_YEAR, year)
        
    def set_email(self, email):
        self.type(self.INPUT_EMAIL, email)
        
    def set_unique_email(self):
        num = random.randint(0,99999999999999999)
        email_address = f"pyta10_{num}@gmail.com"
        self.set_email(email_address)
        
    def set_password(self, text):
        self.type(self.INPUT_PASSWORD, text)

    def set_confirm_password(self, text):
        self.type(self.INPUT_CONFIRM_PASSWORD, text)
        
    def click_register_button(self):
        self.find(self.BUTTON_REGISTER).click()
        
    def is_first_name_error_displayed(self):
        return self.find(self.ERROR_FIRST_NAME).is_displayed()
    
    def is_last_name_error_displayed(self):
        return self.find(self.ERROR_LAST_NAME).is_displayed()

    def is_email_error_displayed(self):
        return self.find(self.ERROR_EMAIL).is_displayed()

    def is_password_error_displayed(self):
        return self.find(self.ERROR_PASS).is_displayed()

    def is_password_confirm_error_displayed(self):
        return self.find(self.ERROR_PASS_CONFIRM).is_displayed()
    
    def is_success_msg_displayed(self):
        return self.find(self.REGISTER_SUCCESS_MESSAGE).is_displayed()
    
    def is_success_msg_correct(self, expected_text):
        return expected_text == self.get_text(self.REGISTER_SUCCESS_MESSAGE)
