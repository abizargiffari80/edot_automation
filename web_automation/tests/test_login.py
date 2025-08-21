import pytest
from web_automation.pages.login_page import LoginPage
from web_automation.config import config


@pytest.mark.smoke
def test_login_success(driver):
    page = LoginPage(driver)
    page.open()
    page.login(config.USERNAME, config.PASSWORD)
    assert page.is_login_successful(), "Login failed: welcome element not visible."


@pytest.mark.negative
@pytest.mark.parametrize("bad_password", ["wrongPassword123", "WRONG", " "])
def test_login_invalid_password(driver, bad_password):
    page = LoginPage(driver)
    page.open()
    page.login(config.USERNAME, bad_password)
    err = page.get_error_message().lower()
    assert any(k in err for k in ["incorrect", "invalid", "wrong"]), f"Unexpected error text: {err}"

