from selenium.webdriver.common.by import By
from utilities.utils import BrowserUtils

class LoginPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        try:
            self.userName = (By.XPATH, "//input[@name='username']")
            self.passWord = (By.XPATH, "//input[@name='password']")
            self.preDefinedUser = (By.CSS_SELECTOR, "div[class='orangehrm-login-form'] p:nth-child(1)")
            self.preDefinedPassword = (By.CSS_SELECTOR, "div[class='orangehrm-login-form'] p:nth-child(2)")
            self.loginBtn = (By.CSS_SELECTOR, "button[type='submit']")
        except Exception as e:
            print(f"Failed to initialize the Login page ---> {e}")

    def fetch_Credentials(self):
        dataDict = {}
        try:
            tempUser = self.driver.find_element(*self.preDefinedUser).text
            tempPass = self.driver.find_element(*self.preDefinedPassword).text

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
            # print("data - ",data["userName"])
            self.driver.find_element(*self.userName).send_keys(data["userName"])
            self.driver.find_element(*self.passWord).send_keys(data["password"])
            self.driver.find_element(*self.loginBtn).click()
        except Exception as e:
            print(f"Failed to click login ---> {e}")