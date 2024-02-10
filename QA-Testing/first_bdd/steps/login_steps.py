from behave import *


@given('I am on the login page')
def step_impl(context):
    context.login_page.open()


@then('The page URL is "{url}"')
def step_impl(context, url):
    assert context.login_page.is_url_correct(url), "Login page url is incorrect"


@when('I enter "{email}" in the email input')
def step_impl(context, email):
    context.login_page.set_email(email)


@when('I enter "{password}" in the password input')
def step_impl(context, password):
    context.login_page.set_password(password)


@when('I click the login button')
def step_impl(context):
    context.login_page.click_login_button()


@then('I should see "No customer account found" message')
def step_impl(context):
    assert context.login_page.is_main_error_msg_displayed(), \
        "Error message not displayed"
    assert (context.login_page.main_error_msg_contains_text
            ("No customer account found")), \
        "Error message does not contain expected text"
