from selenium.webdriver.common.by import By
from utilities.utils import BrowserUtils

class LoginPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        try:
            self.userName = self.driver.find_element(By.XPATH, "//input[@name='username']")
            self.passWord = self.driver.find_element(By.XPATH, "//input[@name='password']")
            self.preDefinedUser = self.driver.find_element(By.CSS_SELECTOR, "div[class='orangehrm-login-form'] p:nth-child(1)")
            self.preDefinedPassword = self.driver.find_element(By.CSS_SELECTOR, "div[class='orangehrm-login-form'] p:nth-child(2)")
            self.loginBtn = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        except Exception as e:
            print(f"Failed to initialize the Login page ---> {e}")

    def fetch_Credentials(self):
        dataDict = {}
        try:
            tempUser = self.preDefinedUser.text
            tempPass = self.preDefinedPassword.text

            userParts = tempUser.split(":")
            passParts = tempPass.split(":")

            if len(userParts) and len(passParts):
                dataDict['userName'] = userParts[1].strip()
                dataDict['password'] = passParts[1].strip()
            else:
                print("Error: Username or password format unexpected.")
        except Exception as e:
            print(f"Failed to fetch credentials ---> {e}")

        return dataDict
    
    def click_login(self, **data):
        try:
            if "userName" not in data and "password" not in data :
                raise ValueError("Missing username and password")
            self.userName.send_keys(data["userName"])
            self.passWord.send_keys(data["password"])
            self.loginBtn.click()
            return True
        except Exception as e:
            print(f"Failed to click login ---> {e}")
            return False