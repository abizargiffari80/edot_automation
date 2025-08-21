import os
from dotenv import load_dotenv

# Load environment variables specific to mobile automation
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

# Mobile automation config values
APPIUM_SERVER_URL = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")
PLATFORM = os.getenv("MOBILE_PLATFORM", "android").lower()

# Android settings
ANDROID_DEVICE_NAME = os.getenv("ANDROID_DEVICE_NAME", "emulator-5554")
ANDROID_PLATFORM_VER = os.getenv("ANDROID_PLATFORM_VERSION", "")
ANDROID_APP_PACKAGE = os.getenv("ANDROID_APP_PACKAGE", "id.edot.ework")
ANDROID_APP_ACTIVITY = os.getenv("ANDROID_APP_ACTIVITY", ".MainActivity")

NEW_COMMAND_TIMEOUT = int(os.getenv("NEW_COMMAND_TIMEOUT", "120"))
AUTO_GRANT_PERMISSIONS = os.getenv("AUTO_GRANT_PERMISSIONS", "1").lower() in {"1", "true", "yes"}
