import os
import pytest
from datetime import datetime

from web_automation.utils.driver_factory import get_driver
from web_automation.config import config as cfg


def pytest_addoption(parser):
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Run with a visible browser window (disables headless).",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Force headless mode on (overrides env/config).",
    )
    parser.addoption(
        "--keep-open",
        action="store_true",
        default=False,
        help="Do not quit the browser at the end of each test (useful for debugging).",
    )


@pytest.fixture(scope="function")
def driver(request):
    # Priority: CLI flags > env var > config default
    if request.config.getoption("--headless"):
        headless = True
    elif request.config.getoption("--headed"):
        headless = False
    else:
        headless_env = os.getenv("HEADLESS")
        headless = cfg.HEADLESS if headless_env is None else headless_env.lower() in {"1", "true", "yes"}

    drv = get_driver(cfg.BROWSER, headless=headless)
    yield drv

    if not request.config.getoption("--keep-open"):
        try:
            drv.quit()
        except Exception:
            pass


def pytest_runtest_makereport(item, call):
    # On test failure, capture a screenshot to artifacts/
    if call.when == "call" and call.excinfo is not None:
        drv = item.funcargs.get("driver")
        if drv:
            os.makedirs("artifacts", exist_ok=True)
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            fname = os.path.join("artifacts", f"{item.name}_{ts}.png")
            try:
                drv.save_screenshot(fname)
                item.add_report_section("call", "screenshot", f"Saved screenshot to {fname}")
            except Exception:
                pass
