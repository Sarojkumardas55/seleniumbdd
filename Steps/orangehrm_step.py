import time

from ReusableMethods.reusable_methods import *
from Driver.Selenium_driver import get_driver
from behave import given, when, then
from selenium.webdriver.common.by import By
from Locators.locators_loader import LocatorsLoader

locators_loader = LocatorsLoader("Locators/locator.json")


@given('I am on the orange hrm login page')
def step_impl(context):
    context.driver = get_driver()
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@when('I enter "{search_text}" into the username')
def step_impl(context, search_text):
    # input_text(context.driver, By.NAME, "username", search_text)
    lc1=locators_loader.get_locator("LoginPage","USERNAME")
    input_text(context.driver,*lc1,search_text)


@when('I enter "{search_text}" into the password')
def step_impl(context, search_text):
    # input_text(context.driver, By.NAME, "password", search_text)
    lc2=locators_loader.get_locator("LoginPage","PASSWORD")
    input_text(context.driver,*lc2,search_text)


@when('I click the login button')
def step_impl(context):
     # click_element(context.driver, By.XPATH, "//button[@type='submit']")
     lc3=locators_loader.get_locator("LoginPage", "LOGIN_BUTTON")
     click_element(context.driver, *lc3)
     time.sleep(3)
    # search_box = context.driver.find_element("name", "q")
    # search_box.submit()