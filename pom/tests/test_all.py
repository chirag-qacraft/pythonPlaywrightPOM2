from pom.pages.all_elements import AllElements
import pytest
from playwright.async_api import expect


@pytest.mark.asyncio
async def test_success_login(browser_setup):
    page =  browser_setup

    success_login_obj = AllElements(page)
    await success_login_obj.success_login()
    await expect(success_login_obj.verify_secure_page).to_be_visible()
    await expect(success_login_obj.verify_secure_page).to_have_text("You logged into a secure area!")


@pytest.mark.asyncio
async def test_invalid_username(browser_setup):
    page =  browser_setup

    invalid_username_obj = AllElements(page)
    await invalid_username_obj.invalid_username()

    await expect(invalid_username_obj.invalid_msg).to_have_text("Your username is invalid!")
    await expect(page).to_have_url("https://practice.expandtesting.com/login")

@pytest.mark.asyncio
async def test_invalid_password(browser_setup):
    page = browser_setup

    invalid_password_obj = AllElements(page)
    await invalid_password_obj.invalid_password()
    await expect(invalid_password_obj.invalid_msg).to_have_text("Your password is invalid!")
    await expect(page).to_have_url("https://practice.expandtesting.com/login")


