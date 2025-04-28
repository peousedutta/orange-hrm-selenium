import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Dashboard:
    def __init__(self, driver):
        super().__init__(driver)
        