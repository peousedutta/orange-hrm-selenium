import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.utils import BrowserUtils


class Dashboard(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        try:
            self.driver = driver
            self.sidePanel_ActionBtns_path = (By.XPATH, "//div[@class='oxd-sidepanel-body']")
            self.sidePanel_myinfbtn = self.driver.find_element(By.XPATH, "//span[normalize-space()='My Info']")
            self.personalDetails_form_path = (By.XPATH, "//div[@class='orangehrm-background-container']")
            self.personalDetails_form_ProfileImage = self.driver.find_element(By.XPATH, "//div[@class='orangehrm-edit-employee-image']//img[@alt='profile picture']")
        except Exception as e:
            print(f"[ERROR] Dashboard initilization failed with error --> {e}")
    
    def perform_click_myinfo(self) -> bool:
        try:
            self.sidePanel_myinfbtn.click()
            return True
        except Exception as e:
            print(f"[ERROR] Myinfo click failed with error --> {e}")
            return False
        
    def check_personal_details_form_present(self) -> bool:
        try:
            elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.personalDetails_form_path))
            if elem:
                return True
            else :
                raise Exception("Peronal details form not found")
        except Exception as e:
            print(f"[ERROR] Myinfo click failed with error --> {e}")
            return False

    def check_profile_image_present(self) -> bool:        
        try:
            self.sidePanel_myinfbtn.click()
            return True
        except Exception as e:
            print(f"[ERROR] Myinfo click failed with error --> {e}")
            return False