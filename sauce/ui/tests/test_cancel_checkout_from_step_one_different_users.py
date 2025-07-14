import pytest

from sauce.test_data.access_data import standard_user, locked_out_user, problem_user, performance_glitch_user, error_user, visual_user, password
from sauce.ui.pages.cart_page import CartPage
from sauce.ui.pages.checkout_step_one_page import CheckoutStepOnePage
from sauce.ui.pages.login_page import LoginPage
from sauce.ui.pages.products_page import ProductsPage


@pytest.mark.parametrize("username,password", [
    (standard_user, password),
    (locked_out_user, password),
    (problem_user, password),
    (performance_glitch_user, password),
    (error_user, password),
    (visual_user, password)
])
def test_cancel_checkout_from_step_one_different_users(set_up, username, password):
    page = set_up
    login = LoginPage(page)
    login.go_to_login_page()
    login.login(username, password)

    products_page = ProductsPage(page)
    products_page.item_add_to_cart()
    products_page.go_to_cart()

    cart_page = CartPage(page)
    cart_page.checkout()

    checkout_step_one = CheckoutStepOnePage(page)
    checkout_step_one.cancel_checkout()

    assert cart_page.title.is_visible(),f"Bei {username} wurde checkout cancel nicht korrekt durchgeführt"
