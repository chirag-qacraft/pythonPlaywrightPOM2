import os
from pom.pages.all_elements import AllElements
import pytest
import pytest_asyncio
from playwright.async_api import expect


@pytest.mark.asyncio
class TestLogin:

    @pytest_asyncio.fixture(scope="function", autouse=True)
    async def setup(self, browser_setup):
        self.page, self.base_url = browser_setup

    async def test_success_login(self):
        try:
            success_login_obj = AllElements(self.page)
            await success_login_obj.success_login()
            await expect(success_login_obj.verify_secure_page).to_be_visible()
            await expect(success_login_obj.verify_secure_page).to_have_text("You logged into a secure area!")

        except Exception as e:
            # Create screenshot folder if it doesn't exist
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")

            ss_path = "screenshots/login_failure_screenshot.png"
            await self.page.screenshot(path=ss_path)
            print(f"Screenshot taken on failure: {ss_path}")
            print(f"Error: {str(e)}")
            pytest.fail(f"Test failed: {str(e)}")

    async def test_invalid_username(self):
        try:
            invalid_username_obj = AllElements(self.page)
            await invalid_username_obj.invalid_username()
            await expect(invalid_username_obj.invalid_msg).to_have_text("Your username is invalid!")
            await expect(self.page).to_have_url(self.base_url)

        except Exception as e:
            # Create screenshot folder if it doesn't exist
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")

            ss_path = "screenshots/invalid_username_failure_screenshot.png"
            await self.page.screenshot(path=ss_path)
            print(f"Screenshot taken on failure: {ss_path}")
            print(f"Error: {str(e)}")
            pytest.fail(f"Test failed: {str(e)}")

    async def test_invalid_password(self):
        try:
            invalid_password_obj = AllElements(self.page)
            await invalid_password_obj.invalid_password()
            await expect(invalid_password_obj.invalid_msg).to_have_text("Your password is invalid!")
            await expect(self.page).to_have_url(self.base_url)

        except Exception as e:
            # Create screenshot folder if it doesn't exist
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")

            ss_path = "screenshots/invalid_password_failure_screenshot.png"
            await self.page.screenshot(path=ss_path)
            print(f"Screenshot taken on failure: {ss_path}")
            print(f"Error: {str(e)}")
            pytest.fail(f"Test failed: {str(e)}")
