import pytest
from playwright.async_api import expect, async_playwright
from pom.pages.invalid_username_elements import InvalidUserName


@pytest.mark.asyncio
async def test_invalid_username():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Launch browser
        context = await browser.new_context()  # Create a new context (similar to a browser profile)
        page = await context.new_page()

        invalid_uname_obj = InvalidUserName(page)

        await invalid_uname_obj.open_browser_invalid_user()
        await invalid_uname_obj.invalid_username()

        await expect(invalid_uname_obj.invalid_msg).to_have_text("Your username is invalid!")
        await expect(page).to_have_url("https://practice.expandtesting.com/login")

