import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope='function')
def browserInstance():
    serviceObj = Service()
    driver = webdriver.Chrome(service=serviceObj)
    driver.implicitly_wait(4)
    yield driver
    driver.close()