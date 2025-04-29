import pytest
from pageObjects.dashboard import Dashboard
from utilities.ReadProperties import ReadConfig
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Test_002_personal_details:
    @pytest.fixture(autouse=True)
    def setup(self, browserInstance):
        self.driver = browserInstance
        self.baseurl = ReadConfig.GetApplicationURL()
        self.dashboard = Dashboard(self.driver)

    def test_perform_login(self):
        print(self.baseurl)
        assert self.dashboard.test_login(self.baseurl), "Test Login Failed"
        self.driver.implicitly_wait(10)

    def test_pageTitle(self):
        assert self.dashboard.check_page_title(), "Page Title not found"
    
    def test_check_view_personal_details_ui(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.dashboard.sidePanel_ActionBtns_path))
        assert self.dashboard.perform_click_myinfo(), "Side Panel myinfo click operation failed"
        assert self.dashboard.check_personal_details_form_present(), "Personal details form not found"
        assert self.dashboard.check_profile_image_present(), "Profile image not found"