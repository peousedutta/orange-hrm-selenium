import os
import sys
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage

URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

def test_e2e(browserInstance):
    driver = browserInstance
    driver.get(URL)
    
    loginPage = LoginPage(driver)
    data = loginPage.fetchCredentials()
    print("data --- ", data)