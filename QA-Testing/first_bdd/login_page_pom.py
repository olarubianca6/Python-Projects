import unittest

from pages.login_page import LoginPage


class LoginTests(unittest.TestCase):

    def test_invalid_login(self):
        login_page = LoginPage()
        login_page.open()
        login_page.set_email("pyta10@gmail.com")
        login_page.set_password("alabala")
        login_page.click_login_button()
        assert login_page.is_main_error_msg_displayed(), "Error message is not displayed"
