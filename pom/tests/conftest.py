import pytest_asyncio
from playwright.async_api import async_playwright


@pytest_asyncio.fixture(scope="function")
async def browser_setup():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://practice.expandtesting.com/login")
        await page.wait_for_load_state("domcontentloaded")
        yield page
        await context.close()

