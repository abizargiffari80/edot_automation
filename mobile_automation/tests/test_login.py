import pytest
from mobile_automation.pages.login_page import MobileLoginPage
from mobile_automation.config import config


@pytest.mark.smoke
def test_mobile_login_success(mobile_driver):
    assert config.COMPANY_ID, "MOBILE_COMPANY_ID is not set! Put it in your .env"
    assert config.USERNAME and config.PASSWORD, "TEST_USERNAME/TEST_PASSWORD not set in .env"

    page = MobileLoginPage(mobile_driver)
    page.login(config.COMPANY_ID, config.USERNAME, config.PASSWORD)
    assert page.is_login_successful(), "Login failed: dashboard marker not visible."
