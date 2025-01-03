from playwright.async_api import Page

class InvalidPassword:
    def __init__(self, page):
        self.page = page
        self.login_button = page.locator("//button[text()='Login']")
        self.username_textbox = page.locator("//input[@id='username']")
        self.password_textbox = page.locator("//input[@id='password']")
        self.verify_secure_page = page.locator("//b[contains(text(),'secure')]")
        self.logout_button = page.locator("//i[contains(text(),'Logout')]")
        self.invalid_msg = page.locator("//b[contains(text(),'invalid!')]")


    async def invalid_password(self):
        await self.username_textbox.fill("practice")
        await self.password_textbox.fill("wrongpassword!")
        await self.login_button.click()