from selenium.webdriver.common.by import By

class LoginLocators:
    userName = (By.XPATH, "//input[@name='username']")
    passWord = (By.XPATH, "//input[@name='password']")
    preDefinedUser = (By.CSS_SELECTOR, "div[class='orangehrm-login-form'] p:nth-child(1)")
    preDefinedPassword = (By.CSS_SELECTOR, "div[class='orangehrm-login-form'] p:nth-child(2)")
