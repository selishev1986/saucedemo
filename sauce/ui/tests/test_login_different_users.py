import pytest

from sauce.test_data.access_data import standard_user, locked_out_user, problem_user, performance_glitch_user, error_user, visual_user, password
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
def test_login_different_users(set_up, username, password):
    page = set_up
    login = LoginPage(page)
    login.go_to_login_page()
    login.login(username, password)

    products_page = ProductsPage(page)

    assert products_page.products_container.is_visible(), f"{username} wurde nicht korrekt angemeldet"
