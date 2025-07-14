from playwright.sync_api import Page


class CartPage():
    def __init__(self, page: Page):
        self.page = page

    # Locators:
    # Product container
        self.products_container = page.locator("[data-test='cart-list']")

    # Continue Shopping button
        self.continue_shopping_button =  page.locator("[data-test='continue-shopping']")

    # Remove button
        self.remove_button = page.get_by_role("button", name="Remove")

    # Checkout button
        self.checkout_button = page.get_by_role("button", name="Checkout")

    # Cart image
        self.cart_image = page.locator("[data-test='shopping-cart-badge']")

    # Title
        self.title = page.get_by_text("Your Cart")


    # Methods:
    # Click Continue Shopping button
    def continue_shopping(self):
        self.continue_shopping_button.click()

        return self

    # Remove product from cart
    def item_remove_from_cart(self):
        self.remove_button.click()

        return self

    # Click checkout button
    def checkout(self):
        self.checkout_button.click()

        return self