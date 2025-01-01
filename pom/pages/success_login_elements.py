import time

from playwright.async_api import Page

class SuccessLogin:
    def __init__(self, page):
        self.page = page
        self.login_button = page.locator("//button[text()='Login']")
        self.username_textbox = page.locator("//input[@id='username']")
        self.password_textbox = page.locator("//input[@id='password']")
        self.verify_secure_page = page.locator("//b[contains(text(),'secure')]")
        self.logout_button = page.locator("//i[contains(text(),'Logout')]")


    async def cre_success_login(self):
        await self.username_textbox.fill("practice")
        await self.password_textbox.fill("SuperSecretPassword!")
        await self.login_button.click()

    async def logout_sl(self):
        await self.logout_button.click()






