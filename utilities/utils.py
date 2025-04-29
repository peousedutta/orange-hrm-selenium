from utilities.ReadProperties import ReadConfig

class BrowserUtils:
    def __init__(self, driver):
        self.driver = driver

    def check_page_title(self) -> bool:
        try:
            title = ReadConfig.GetWebsitetitle()
            print("title - ",self.driver.title)
            if title == self.driver.title:
                return True
            else:
                raise Exception("Error fetching title")
        except Exception as e:
            print(f"page title not found {e}")
            return False

    def check_responsiveness(self) -> bool:
        pass

    def test_login(self, url: str) -> bool:
        try:
            print(f"[INFO] Navigating to: {url}")
            self.driver.get(url)

            from pageObjects.login_page import LoginPage

            username = ReadConfig.GetUsername()
            password = ReadConfig.GetPassword()
            print(f"[DEBUG] Username: {username}, Password: {password}")

            login_page = LoginPage(self.driver)
            login_success = login_page.click_login(username, password)

            if not login_success:
                print("[ERROR] Login button click or login process failed.")
            return login_success
        except Exception as e:
            print(f"[ERROR] Login test failed: {e}")
            return False
