from appium import webdriver
from selenium.webdriver.chrome.options import Options
from mobile_automation.config import config as cfg


def build_android_caps():
    caps = {
        "platformName": "Android",                 # Specify platform as Android
        "automationName": "UiAutomator2",          # Use UiAutomator2 for Android automation
        "deviceName": cfg.ANDROID_DEVICE_NAME,     # Your LDPlayer device name
        "newCommandTimeout": cfg.NEW_COMMAND_TIMEOUT,  # Timeout for commands
        "autoGrantPermissions": cfg.AUTO_GRANT_PERMISSIONS,  # Auto grant permissions if necessary
    }

    if cfg.ANDROID_PLATFORM_VER:
        caps["platformVersion"] = cfg.ANDROID_PLATFORM_VER

    # Launch the installed app via package/activity
    if cfg.ANDROID_APP_PACKAGE and cfg.ANDROID_APP_ACTIVITY:
        caps["appPackage"] = cfg.ANDROID_APP_PACKAGE        # The package name of your app (eWork)
        caps["appActivity"] = cfg.ANDROID_APP_ACTIVITY      # The main activity of the app

    # Ensure that browserName and goog:chromeOptions are NOT set anywhere (if accidentally set)
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
