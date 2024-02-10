from browser import Browser
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.register_page = RegisterPage()
    

def after_all(context):
    context.browser.close()