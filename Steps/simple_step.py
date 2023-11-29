import time

from ReusableMethods.reusable_methods import *
from Driver.Selenium_driver import get_driver
from behave import given, when, then
from selenium.webdriver.common.by import By


# @given('I am on the Google search page')
# def step_impl(context):
#     context.driver = get_driver()
#     context.driver.get("https://www.google.com")
#
# @when('I enter "{search_text}" into the search bar')
# def step_impl(context, search_text):
#     search_box = context.driver.find_element("name", "q")
#     search_box.send_keys(search_text)
#
# @when('I click the search button')
# def step_impl(context):
#     search_box = context.driver.find_element("name", "q")
#     search_box.submit()
#
# @then('I should see search results')
# def step_impl(context):
#     assert "Google Search" in context.driver.title


@given('I am on the Google search page')
def step_impl(context):
    context.driver = get_driver()
    context.driver.get("https://www.google.com")


@when('I enter "{search_text}" into the search bar')
def step_impl(context, search_text):
    input_text(context.driver, By.NAME, "q", search_text)


@when('I click the search button')
def step_impl(context):
    # click_element(context.driver, By.NAME, "q")
    # time.sleep(3)
    search_box = context.driver.find_element("name", "q")
    search_box.submit()


@then('I should see search results')
def step_impl(context):
    assert "Google Search" in context.driver.title


# check the element is available and click
@when('I click the search button if present')
def step_impl(context):
    if is_element_present(context.driver, By.NAME, "q"):
        click_element(context.driver, By.NAME, "q")
    else:
        print("Search button is not present")


# select the element from dropdown
@when('I select "{option_text}" from the dropdown')
def step_impl(context, option_text):
    select_from_dropdown(context.driver, By.ID, "dropdown-id", option_text)


@when('I accept the alert')
def step_impl(context):
    accept_alert(context.driver)


@when('I reject the alert')
def step_impl(context):
    reject_alert(context.driver)


@when('I switch to the frame with "{frame_id}"')
def step_impl(context, frame_id):
    switch_to_frame(context.driver, By.ID, frame_id)


@when('I take a screenshot and save it to "{file_path}"')
def step_impl(context, file_path):
    take_screenshot(context.driver, file_path)


@when('I switch back to the default content')
def step_impl(context):
    switch_to_default_content(context.driver)


@then('the element with ID "{element_id}" should be enabled')
def step_impl(context, element_id):
    assert is_element_enabled(context.driver, By.ID, element_id), f"Element with ID {element_id} is not enabled"