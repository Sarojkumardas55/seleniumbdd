import json
from selenium.webdriver.common.by import By

import json
from selenium.webdriver.common.by import By

class LocatorsLoader:
    def __init__(self, file_path):
        with open(file_path, 'r') as file:
            self.locators_data = json.load(file)

    def get_locator(self, page_name, element_name):
        page_data = self.locators_data.get(page_name, {})
        element_data = page_data.get(element_name)
        if element_data:
            by = getattr(By, element_data[0].upper())
            value = element_data[1]
            return by, value
        return None

