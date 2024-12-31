import pytest
from playwright.async_api import expect, async_playwright
from pom.pages.success_login_elements import SuccessLogin


@pytest.mark.asyncio
async def test_success_login():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Launch browser
        context = await browser.new_context()  # Create a new context (similar to a browser profile)
        page = await context.new_page()


        success_obj = SuccessLogin(page)
        await success_obj.open_browser_success_login()
        await success_obj.cre_success_login()

        await expect(success_obj.verify_secure_page).to_be_visible()
        await expect(success_obj.verify_secure_page).to_have_text("You logged into a secure area!")

        await success_obj.logout_sl()



