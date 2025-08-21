# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
#
# def get_driver(browser_name="chrome"):
#     if browser_name.lower() != "chrome":
#         raise Exception(f"Browser '{browser_name}' is not supported! Only Chrome is available.")
#
#     # Path to chromedriver (inside "drivers" folder in project root)
#     chrome_driver = os.path.join("drivers", "chromedriver.exe")
#
#     options = Options()
#     options.add_argument("--start-maximized")
#
#     service = Service(executable_path=chrome_driver)
#     driver = webdriver.Chrome(service=service, options=options)
#     driver.implicitly_wait(10)
#     return driver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_driver(browser_name: str = "chrome", headless: bool = False):
    """
    Returns a ready-to-use Selenium WebDriver.
    - Uses webdriver-manager to auto-install the matching ChromeDriver.
    - Supports headless mode for CI.
    """
    if browser_name.lower() != "chrome":
        raise Exception(f"Browser '{browser_name}' is not supported! Only Chrome is available.")

    options = Options()
    if headless:
        # new headless for Chrome 109+
        options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-notifications")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)  # keep implicit small; rely on explicit waits in Pages
    return driver
