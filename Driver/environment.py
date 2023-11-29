from Driver.Selenium_driver import get_driver
from behave import fixture, use_fixture
from allure_behave.hooks import allure_report

# @fixture
# def selenium_browser_chrome(context):
#     context.driver = get_driver()
#     yield context.driver
#     context.driver.quit()
#
# def before_all(context):
#     use_fixture(selenium_browser_chrome, context)
# from selenium_driver import get_driver
from behave import fixture, use_fixture
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.common.exceptions import WebDriverException
import os


# Define a custom event listener for WebDriver events
class ScreenshotListener(AbstractEventListener):
    def on_exception(self, exception, driver):
        try:
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, "failure_screenshot.png")
            driver.save_screenshot(screenshot_path)
            print(f"Screenshot captured: {screenshot_path}")
        except WebDriverException as e:
            print(f"Failed to capture screenshot: {e}")


@fixture
def selenium_browser_chrome(context):
    driver = get_driver()
    # Wrap the driver with EventFiringWebDriver and attach the custom listener
    context.driver = EventFiringWebDriver(driver, ScreenshotListener())
    yield context.driver
    context.driver.quit()


def before_all(context):
    use_fixture(selenium_browser_chrome, context)
    allure_report("C:\Users\saroj.das\PycharmProjects\seleniumbdd\report")
