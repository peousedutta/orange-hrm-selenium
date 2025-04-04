from selenium.webdriver.common.by import By

class LoginLocators():
    def __init__(self):
        self.userName = (By.XPATH, "//input[@name='username']")
        self.passWord = (By.XPATH, "//input[@name='password]")