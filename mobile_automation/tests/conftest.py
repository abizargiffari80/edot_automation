import os
import pytest
from datetime import datetime
from mobile_automation.utils.appium_factory import get_mobile_driver
from mobile_automation.config import config as cfg


def pytest_addoption(parser):
    parser.addoption(
        "--platform",
        action="store",
        default=None,
        help="Mobile platform to run on: android (LDPlayer).",
    )
    parser.addoption(
        "--keep-open",
        action="store_true",
        default=False,
        help="Do not quit the Appium session at the end of each test (debugging).",
    )


@pytest.fixture(scope="function")
def mobile_driver(request):
    platform_cli = request.config.getoption("--platform")
    platform_env = os.getenv("MOBILE_PLATFORM")
    platform = platform_cli or platform_env or cfg.PLATFORM

    drv = get_mobile_driver(platform)
    yield drv

    if not request.config.getoption("--keep-open"):
        try:
            drv.quit()
        except Exception:
            pass


def pytest_runtest_makereport(item, call):
    if call.when == "call" and call.excinfo is not None:
        drv = item.funcargs.get("mobile_driver")
        if drv:
            os.makedirs("artifacts", exist_ok=True)
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            fname = os.path.join("artifacts", f"mobile_{item.name}_{ts}.png")
            try:
                drv.save_screenshot(fname)
                item.add_report_section("call", "screenshot", f"Saved screenshot to {fname}")
            except Exception:
                pass
