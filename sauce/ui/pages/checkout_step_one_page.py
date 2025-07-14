from playwright.sync_api import Page

from sauce.test_data.access_data import firstname, lastname, zip_code
from sauce.ui.pages.checkout_step_two_page import CheckoutStepTwoPage


class CheckoutStepOnePage():
    def __init__(self, page: Page):
        self.page = page

    # Locators:
    # Checkout info container
        self.checkout_info_container = page.locator("[data-test='checkout-info-container']")

    # Continue button
        self.continue_button =  page.locator("[data-test='continue']")

    # Cancel button
        self.cancel_button = page.locator("[data-test='cancel']")

    # First Name field
        self.firstname_field = page.locator("[data-test='firstName']")

    # Last Name field
        self.lastname_field = page.locator("[data-test='lastName']")

    # Zip/Postal Code field
        self.zip_field = page.locator("[data-test='postalCode']")


    # Methods:
    # Click continue checkout button
    def continue_checkout(self):
        self.continue_button.click()

        return self

    # Click cancel button
    def cancel_checkout(self):
        self.cancel_button.click()

        return self

    # Fill form
    def fill_form(self):
        self.firstname_field.fill(firstname)
        self.lastname_field.fill(lastname)
        self.zip_field.fill(zip_code)

        return CheckoutStepTwoPage