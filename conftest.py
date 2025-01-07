import pytest_asyncio
from playwright.async_api import async_playwright


@pytest_asyncio.fixture(scope="function")
async def browser_setup():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.set_viewport_size({"width": 1920, "height": 1080})
        base_url = "https://practice.expandtesting.com/login"
        await page.goto(base_url)
        await page.wait_for_load_state("domcontentloaded")
        yield page, base_url
        await context.close()

