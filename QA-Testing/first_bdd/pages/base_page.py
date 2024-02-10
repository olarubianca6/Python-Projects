from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser import Browser


class BasePage(Browser):

    INPUT_SEARCH = (By.ID, "small-searchterms")
    BUTTON_SEARCH = (By.XPATH, "//button[text()='Search']")

    def find(self, locator):
        return self.driver.find_element(*locator)

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def select_by_text(self, locator, text):
        dropdown = Select(self.find(locator))
        dropdown.select_by_visible_text(text)

    def select_by_index(self, locator, index):
        dropdown = Select(self.find(locator))
        dropdown.select_by_index(index)

    def is_url_correct(self, expected_url):
        return self.driver.current_url == expected_url

    def set_search_term(self, text):
        self.type(self.INPUT_SEARCH, text)

    def click_search_button(self):
        self.find(self.BUTTON_SEARCH).click()
