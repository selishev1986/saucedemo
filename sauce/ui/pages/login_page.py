
from playwright.sync_api import Page

from sauce.ui.constants.constants import login_page_url
from sauce.ui.pages.products_page import ProductsPage


class LoginPage():
    def __init__(self, page: Page):
        self.page = page

    # Locators:
        # Username field
        self.username_field = page.locator("[data-test='username']")

        # Password field
        self.password_field = page.locator("[data-test='password']")

        # Login button
        self.login_button = page.locator("[data-test='login-button']")


    # Methods:
    def go_to_login_page(self):
        self.page.goto(login_page_url)

        return self

    def login(self, name, password):
        self.username_field.fill(name)
        self.password_field.fill(password)
        self.login_button.click()

        return ProductsPage