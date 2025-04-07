import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
import sys
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@pytest.fixture(scope='function')
def browserInstance():
    serviceObj = Service()
    driver = webdriver.Chrome(service=serviceObj)
    driver.implicitly_wait(4)
    yield driver
    driver.close()