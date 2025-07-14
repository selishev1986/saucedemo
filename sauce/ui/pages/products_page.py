from xmlrpc.client import Boolean

from playwright.sync_api import Page

from sauce.ui.pages.cart_page import CartPage
from sauce.ui.pages.product_page import ProductPage


class ProductsPage():
    def __init__(self, page: Page):
        self.page = page

    # Locators:
    # Container with all products
        self.products_container = page.locator("[data-test='inventory-container']")

    # Product link
        self.product_link = page.locator("[data-test='inventory-item-name']")

    # Add to cart button
        self.add_to_cart_button = page.get_by_role("button", name="Add to cart")

    # Remove button
        self.remove_button = page.get_by_role("button", name="Remove")

    # Menu button
        self.menu_button = page.get_by_role("button", name="Open Menu")

    # Logout link
        self.logout_link = page.locator("[data-test='logout-sidebar-link']")

    # Cart image
        self.cart_image = page.locator("[data-test='shopping-cart-badge']")


    # Methods:
    # Go to product page
    def go_to_product_page(self):
        self.product_link.first.click()

        return ProductPage

    # Product add to cart
    def item_add_to_cart(self):
        self.add_to_cart_button.first.click()

        return self

    # Remove product from cart
    def item_remove_from_cart(self):
        self.remove_button.first.click()

        return self

    # Cart checking
    def checking_cart(self):
        self.cart_image.is_visible()

        return Boolean

    # Logout
    def logout(self):
        self.menu_button.click()
        self.logout_link.click()

        return self

    # Go to cart
    def go_to_cart(self):
        self.cart_image.click()

        return CartPage
