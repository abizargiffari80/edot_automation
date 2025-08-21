import os

# Optional: load .env
try:
    from dotenv import load_dotenv  # type: ignore
    load_dotenv()
except Exception:
    pass

# ----- Shared creds (reuse from your web .env) -----
USERNAME = os.getenv("TEST_USERNAME", "")
PASSWORD = os.getenv("TEST_PASSWORD", "")
COMPANY_ID = os.getenv("MOBILE_COMPANY_ID", "")

# ----- Appium server & platform -----
APPIUM_SERVER_URL = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")
PLATFORM = os.getenv("MOBILE_PLATFORM", "android").lower()

# ----- ANDROID settings -----
ANDROID_DEVICE_NAME  = os.getenv("ANDROID_DEVICE_NAME", "emulator-5554")  # set to your LDPlayer adb name
ANDROID_PLATFORM_VER = os.getenv("ANDROID_PLATFORM_VERSION", "")          # e.g., "14"
ANDROID_APP_PACKAGE  = os.getenv("ANDROID_APP_PACKAGE", "id.edot.ework")  # Updated app package name
ANDROID_APP_ACTIVITY = os.getenv("ANDROID_APP_ACTIVITY", "id.edot.onboarding.ui.splash.SplashScreenActivity")  # Updated main activity

NEW_COMMAND_TIMEOUT = int(os.getenv("NEW_COMMAND_TIMEOUT", "120"))
AUTO_GRANT_PERMISSIONS = os.getenv("AUTO_GRANT_PERMISSIONS", "1").lower() in {"1", "true", "yes"}
