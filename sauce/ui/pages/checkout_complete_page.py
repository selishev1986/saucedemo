from playwright.sync_api import Page


class CheckoutCompletePage():
    def __init__(self, page: Page):
        self.page = page

    # Locators:
    # Checkout complete header
        self.checkout_summary_container = page.get_by_text("Thank you for your order!")


    # Methods: