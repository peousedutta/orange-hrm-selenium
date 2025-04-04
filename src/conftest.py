import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def browerInstance():
    serviceObj = Service()
    driver = webdriver.Chrome(service=serviceObj)
    driver.implicitly_wait(4)
    yield
    driver.close()