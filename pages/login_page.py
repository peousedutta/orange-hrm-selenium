from locators.login_page_locators import LoginLocators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def fetchCredentials(self):
        dataDict = {}
        try:
            tempUser = self.driver.find_element(*LoginLocators.preDefinedUser).text
            tempPass = self.driver.find_element(*LoginLocators.preDefinedPassword).text

            userParts = tempUser.split(":")
            passParts = tempPass.split(":")

            if len(userParts) and len(passParts):
                dataDict['userName'] = userParts[1].strip()
                dataDict['password'] = passParts[1].strip()
            else:
                print("Error: Username or password format unexpected.")
        except Exception as e:
            print(f"[LoginPage] Failed to fetch credentials: {e}")

        return dataDict