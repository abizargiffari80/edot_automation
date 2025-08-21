# import os
#
# # Optional: load .env if present (for local dev). Safe to ignore if python-dotenv not installed.
# try:
#     from dotenv import load_dotenv  # type: ignore
#     load_dotenv()
# except Exception:
#     pass
#
# BASE_URL = os.getenv("BASE_URL", "https://esuite.edot.id/")
# USERNAME = os.getenv("TEST_USERNAME", "it.qa@edot.id")
# PASSWORD = os.getenv("TEST_PASSWORD", "it.QA2025")
# BROWSER  = os.getenv("BROWSER", "chrome")
#
# # Headless toggle: "1", "true", "yes" enable headless
# HEADLESS = os.getenv("HEADLESS", "1").lower() in {"1", "true", "yes"}

import os
from dotenv import load_dotenv

# Load environment variables specific to web automation
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

# Web automation config values
BASE_URL = os.getenv("BASE_URL", "")
USERNAME = os.getenv("TEST_USERNAME", "")
PASSWORD = os.getenv("TEST_PASSWORD", "")
BROWSER = os.getenv("BROWSER", "chrome")
HEADLESS = os.getenv("HEADLESS", "1")
