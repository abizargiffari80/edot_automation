import os

# Optional: load .env if present (for local dev). Safe to ignore if python-dotenv not installed.
try:
    from dotenv import load_dotenv  # type: ignore
    load_dotenv()
except Exception:
    pass

BASE_URL = os.getenv("BASE_URL", "https://esuite.edot.id/")
USERNAME = os.getenv("TEST_USERNAME", "it.qa@edot.id")
PASSWORD = os.getenv("TEST_PASSWORD", "it.QA2025")
BROWSER  = os.getenv("BROWSER", "chrome")

# Headless toggle: "1", "true", "yes" enable headless
HEADLESS = os.getenv("HEADLESS", "1").lower() in {"1", "true", "yes"}
