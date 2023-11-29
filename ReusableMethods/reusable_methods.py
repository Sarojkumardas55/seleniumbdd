from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoAlertPresentException, \
    NoSuchFrameException


# For click on a web element
def click_element(driver, by, value):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((by, value))
        )
        element.click()
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception while clicking element: {e}")


# For send the text to a text box
def input_text(driver, by, value, text):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((by, value))
        )
        element.send_keys(text)
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception while inputting text: {e}")


# For getting the text of a web element

def get_text(driver, by, value):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((by, value))
        )
        return element.text
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception while getting text: {e}")
        return None  # Return None or handle the exception according to your needs


# For checking the web element is present in the webpage or not
def is_element_present(driver, by, value):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((by, value))
        )
        return True
    except TimeoutException:
        return False


# For selecting the element from dropdown by visible text
def select_from_dropdown(driver, by, value, option_text):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((by, value))
        )
        dropdown = Select(element)
        dropdown.select_by_visible_text(option_text)
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception while selecting from dropdown: {e}")


# For accept the alert

def accept_alert(driver):
    try:
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert.accept()
    except NoAlertPresentException as e:
        print(f"Exception while accepting alert: {e}")


# For accept the alert

def reject_alert(driver):
    try:
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert.dismiss()
    except NoAlertPresentException as e:
        print(f"Exception while accepting alert: {e}")


def switch_to_frame(driver, by, value):
    try:
        frame = WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((by, value))
        )
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception while switching to frame: {e}")


def take_screenshot(driver, file_path):
    try:
        driver.save_screenshot(file_path)
    except Exception as e:
        print(f"Exception while taking screenshot: {e}")


def switch_to_default_content(driver):
    try:
        driver.switch_to.default_content()
    except NoSuchFrameException as e:
        print(f"Exception while switching to default content: {e}")


def is_element_enabled(driver, by, value):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((by, value))
        )
        return element.is_enabled()
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception while checking if element is enabled: {e}")
        return False

