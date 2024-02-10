from behave import *


@given('I am on the register page')
def step_impl(context):
    context.register_page.open()
    
    
@when('I enter "{new_email}" in the register email input')
def step_impl(context, new_email):
    context.register_page.set_email(new_email)
    
    
@when("I click the register button")
def step_impl(context):
    context.register_page.click_register_button()


@then("First name error id displayed")
def step_impl(context):
    assert context.register_page.is_first_name_error_displayed()
    

@then("Last name error is displayed")
def step_impl(context):
    assert context.register_page.is_last_name_error_displayed()


@then("Email error is displayed")
def step_impl(context):
    assert context.register_page.is_email_error_displayed()


@then("Password error is displayed")
def step_impl(context):
    assert context.register_page.is_password_error_displayed()


@then("Password confirm error is displayed")
def step_impl(context):
    assert context.register_page.is_password_confirm_error_displayed()
    
    
@when('I enter "{first_name}" in the first name input')
def step_impl(context, first_name):
    context.register_page.set_first_name(first_name)
    

@when('I enter "{last_name}" in the last name input')
def step_impl(context, last_name):
    context.register_page.set_last_name(last_name)
    
    
@when("I enter a unique email address in the email input")
def step_impl(context):
    context.register_page.set_unique_email()
    

@when('I select "{day}" as my birth day')
def step_impl(context, day):
    context.register_page.select_day_of_birth(day)


@when('I select "{month}" as my birth month')
def step_impl(context, month):
    context.register_page.select_month_of_birth(month)


@when('I select "{year}" as my birth year')
def step_impl(context, year):
    context.register_page.select_year_of_birth(year)


@when('I enter "{password}" in the new password input')
def step_impl(context, password):
    context.register_page.set_password(password)


@when('I enter "{confirm_password}" in the password confirm input')
def step_impl(context, confirm_password):
    context.register_page.set_confirm_password(confirm_password)
    
    
@then("Success message is displayed")
def step_impl(context):
    assert context.register_page.is_success_msg_displayed()
    
    
@then('The success message is "{message}"')
def step_impl(context, message):
    context.register_page.is_success_msg_correct(message)
    
    
@then('The register page URL is "{url}"')
def step_impl(context, url):
    assert context.register_page.is_url_correct(url)
