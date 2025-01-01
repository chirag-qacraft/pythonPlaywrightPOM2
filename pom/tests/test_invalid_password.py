import pytest
from playwright.async_api import expect, async_playwright
from pom.pages.invalid_password_elements import InvalidPassword


@pytest.mark.asyncio
async def test_invalid_password():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Launch browser
        context = await browser.new_context()  # Create a new context (similar to a browser profile)
        page = await context.new_page()
        await  page.goto("https://practice.expandtesting.com/login")

        pwd_obj = InvalidPassword(page)
        await pwd_obj.invalid_password()

        await expect(pwd_obj.invalid_msg).to_have_text("Your password is invalid!")
        await expect(page).to_have_url("https://practice.expandtesting.com/login")