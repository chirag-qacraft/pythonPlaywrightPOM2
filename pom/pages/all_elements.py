from playwright.async_api import Page

class AllElements:
    def __init__(self, page:Page):
        self.page = page
        self.login_button = page.locator("//button[text()='Login']")
        self.username_textbox = page.locator("//input[@id='username']")
        self.password_textbox = page.locator("//input[@id='password']")
        self.verify_secure_page = page.locator("//b[contains(text(),'secure')]")
        self.logout_button = page.locator("//i[contains(text(),'Logout')]")
        self.verify_secure_page = page.locator("//b[contains(text(),'secure')]")
        self.invalid_msg = page.locator("//b[contains(text(),'invalid!')]")

    async def success_login(self):
        await self.username_textbox.fill("practice")
        await self.password_textbox.fill("SuperSecretPassword!")
        await self.login_button.click()

    async def invalid_username(self):
        await self.username_textbox.fill("wrongUser")
        await self.password_textbox.fill("SuperSecretPassword!")
        await self.login_button.click()

    async def invalid_password(self):
        await self.username_textbox.fill("practice")
        await self.password_textbox.fill("wrongpassword")
        await self.login_button.click()
