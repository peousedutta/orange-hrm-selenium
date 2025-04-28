from pageObjects.login_page import LoginPage
from utilities.ReadProperties import ReadConfig
import pytest

class Test_001_login:
    URL = ReadConfig.GetApplicationURL()

    def test_pageTitle(self):
        pass
    
    def test_login(self, browserInstance):
        self.driver = browserInstance
        self.driver.get(self.URL)
        self.loginPage = LoginPage(self.driver)
        # assert self.loginPage.locate_Credentials()
        data = self.loginPage.fetch_Credentials()
        assert self.loginPage.click_login(**data), "Unable to Login"