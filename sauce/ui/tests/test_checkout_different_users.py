import pytest

from sauce.test_data.access_data import standard_user, locked_out_user, problem_user, performance_glitch_user, error_user, visual_user, password
from sauce.ui.pages.cart_page import CartPage
from sauce.ui.pages.checkout_complete_page import CheckoutCompletePage
from sauce.ui.pages.checkout_step_one_page import CheckoutStepOnePage
from sauce.ui.pages.checkout_step_two_page import CheckoutStepTwoPage
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
def test_checkout_different_users(set_up, username, password):
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
    checkout_step_one.fill_form()
    checkout_step_one.continue_checkout()

    checkout_step_two = CheckoutStepTwoPage(page)
    checkout_step_two.finish_checkout()

    checkout_complete = CheckoutCompletePage(page)

    assert checkout_complete.checkout_summary_container.is_visible(),f"Bei {username} wurde checkout nicht korrekt durchgeführt"
