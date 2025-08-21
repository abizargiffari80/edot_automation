from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mobile_automation.config import config


class MobileLoginPage:
    """Page Object for eWork login screen.
    NOTE: Update locators below to match your app's resource-ids or accessibility ids.
    You can inspect with: `adb shell dumpsys window | findstr mCurrentFocus` + UIAutomatorViewer/Appium Inspector.
    """
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        # ----- LOCATORS (PLACEHOLDERS: update IDs to real ones) -----
        self.company_id_input = (AppiumBy.ID, "com.example.ework:id/company_id")  # UPDATE
        self.username_input   = (AppiumBy.ID, "com.example.ework:id/username")    # UPDATE
        self.password_input   = (AppiumBy.ID, "com.example.ework:id/password")    # UPDATE
        self.login_button     = (AppiumBy.ID, "com.example.ework:id/login_btn")   # UPDATE
        self.dashboard_marker = (AppiumBy.ACCESSIBILITY_ID, "home_title")         # UPDATE (some stable element after login)

        # Optional permission dialog
        self.permission_allow = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")  # may vary by ROM

    def login(self, company_id: str, username: str, password: str):
        # Fill Company ID
        cid = self.wait.until(EC.visibility_of_element_located(self.company_id_input))
        cid.clear(); cid.send_keys(company_id)

        # Fill Username
        u = self.wait.until(EC.visibility_of_element_located(self.username_input))
        u.clear(); u.send_keys(username)

        # Fill Password
        p = self.wait.until(EC.visibility_of_element_located(self.password_input))
        p.clear(); p.send_keys(password)

        # Tap Login
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

        # Handle location permission if it appears
        try:
            self.wait.until(EC.element_to_be_clickable(self.permission_allow)).click()
        except Exception:
            pass
        return self

    def is_login_successful(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(self.dashboard_marker))
            return True
        except Exception:
            return False
