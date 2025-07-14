from xmlrpc.client import Boolean

from playwright.sync_api import Page


class ProductPage():
    def __init__(self, page: Page):
        self.page = page

    # Locators:
    # Product container
        self.product_container = page.locator("[data-test='inventory-item']")

    # Add to cart button
        self.add_to_cart_button = page.get_by_role("button", name="Add to cart")

    # Remove button
        self.remove_button = page.get_by_role("button", name="Remove")

    # Cart image
        self.cart_image = page.locator("[data-test='shopping-cart-badge']")


    # Methods:
    # Product add to cart
    def item_add_to_cart(self):
        self.add_to_cart_button.click()

        return self

    # Remove product from cart
    def item_remove_from_cart(self):
        self.remove_button.click()

        return self

    # Cart checking
    def checking_cart(self):
        self.cart_image.is_visible()

        return Boolean
