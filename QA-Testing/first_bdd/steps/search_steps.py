from behave import *


@when('I enter "{text}" in the search input')
def step_impl(context):
    context.set_search_term(text)


@when("I click the search button")
def step_impl(context):
    context.click_search_button()


@then("I get at least one result")
def step_impl(context):
    context.is_result_displayed()


@when('I enter "{text}" in the search input')
def step_impl(context):
    context.set_search_term(text)


@when("I click the search button")
def step_impl(context):
    context.click_search_button()


@then("Error message is displayed")
def step_impl(context):
    context.is_error_msg_displayed()

    
@then('The error message is "{message}"')
def step_impl(context):
    context.is_error_msg_correct()