from appium import webdriver
from selenium.webdriver.chrome.options import Options
from mobile_automation.config import config as cfg


def build_android_caps():
    caps = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": cfg.ANDROID_DEVICE_NAME,
        "newCommandTimeout": cfg.NEW_COMMAND_TIMEOUT,
        "autoGrantPermissions": cfg.AUTO_GRANT_PERMISSIONS,
    }

    if cfg.ANDROID_PLATFORM_VER:
        caps["platformVersion"] = cfg.ANDROID_PLATFORM_VER

    # Prefer launching installed app via package/activity (fast)
    if cfg.ANDROID_APP_PACKAGE and cfg.ANDROID_APP_ACTIVITY:
        caps["appPackage"] = cfg.ANDROID_APP_PACKAGE
        caps["appActivity"] = cfg.ANDROID_APP_ACTIVITY

    # Remove any browser-related capabilities like `browserName` and `goog:chromeOptions`
    if "browserName" in caps:
        del caps["browserName"]

    if "goog:chromeOptions" in caps:
        del caps["goog:chromeOptions"]

    return caps


def get_mobile_driver(platform: str | None = None):
    platform = (platform or cfg.PLATFORM).lower()

    if platform != "android":
        raise ValueError("This scaffold currently targets Android (LDPlayer). Set MOBILE_PLATFORM=android.")

    caps = build_android_caps()

    # Create the options object
    options = Options()

    # Add capabilities to the options
    for key, value in caps.items():
        options.set_capability(key, value)

    # Start the driver
    driver = webdriver.Remote(
        command_executor=cfg.APPIUM_SERVER_URL,
        options=options  # Now we pass options with the capabilities
    )

    driver.implicitly_wait(5)
    return driver
