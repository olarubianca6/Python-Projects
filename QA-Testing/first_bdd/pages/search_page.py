from selenium.webdriver.common.by import By

from base_page import BasePage


class SearchPage(BasePage):

    NO_PRODUCTS_ERROR_MESSAGE = (By.CLASS_NAME, "no-result")
    SEARCH_RESULT = (By.CLASS_NAME, "product-item")

    def is_result_displayed(self):
        return self.find(self.SEARCH_RESULT).is_displayed()

    def is_error_msg_displayed(self):
        return self.find(self.NO_PRODUCTS_ERROR_MESSAGE).is_displayed()

    def is_error_msg_correct(self, expected_text):
        return expected_text == self.get_text(self.NO_PRODUCTS_ERROR_MESSAGE)