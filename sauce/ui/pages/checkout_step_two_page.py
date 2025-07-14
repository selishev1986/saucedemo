from playwright.sync_api import Page


class CheckoutStepTwoPage():
    def __init__(self, page: Page):
        self.page = page

    # Locators:
    # Checkout summary container
        self.checkout_summary_container = page.locator("[data-test='checkout_summary_container']")

    # Finish button
        self.finish_button =  page.locator("[data-test='finish']")

    # Cancel button
        self.cancel_button = page.locator("[data-test='cancel']")


    # Methods:
    # Click finish button
    def finish_checkout(self):
        self.finish_button.click()

        return self

    # Click cancel button
    def cancel_checkout(self):
        self.cancel_button.click()

        return self