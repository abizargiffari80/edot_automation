from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_automation.config import config


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = config.BASE_URL.rstrip("/")
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.use_email_button = (By.XPATH, "//button[normalize-space()='Use Email or Username']")
        self.username_field   = (By.XPATH, "//input[@placeholder='Input Email or Username']")
        self.password_field   = (By.XPATH, "//input[@placeholder='Password']")
        self.login_button     = (By.XPATH, "//button[normalize-space()='Log In']")

        # Success / error indicators (tweak to your DOM if needed)
        self.welcome_text     = (
            By.XPATH,
            "//span[contains(@class,'text-md') and (contains(.,'Welcome') or contains(@class,'text-gray-400'))]"
        )
        self.error_message    = (By.XPATH, "//p[contains(@class,'text-red-500')]")

    def open(self):
        self.driver.get(self.url)

    def login(self, username: str, password: str):
        # Click "Use Email or Username"
        self.wait.until(EC.element_to_be_clickable(self.use_email_button)).click()

        # Enter username then click Log In
        username_el = self.wait.until(EC.visibility_of_element_located(self.username_field))
        username_el.clear()
        username_el.send_keys(username)
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

        # Enter password then click Log In
        password_el = self.wait.until(EC.visibility_of_element_located(self.password_field))
        password_el.clear()
        password_el.send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()
        return self

    def is_login_successful(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(self.welcome_text))
            return True
        except Exception:
            return False

    def get_error_message(self) -> str:
        return self.wait.until(EC.visibility_of_element_located(self.error_message)).text.strip()
