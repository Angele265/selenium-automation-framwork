from pages.home_page import HomePage
from pages.products_page import ProductSearch
from pages.cart_page import CartPage

def test_remove_product_from_cart(driver):
    home_page = HomePage(driver)
    product_page = ProductSearch(driver)
    cart_page = CartPage(driver)

    home_page.open()

    product_page.click_products_button()

    product_page.add_item_to_cart()

    home_page.click_cart()

    assert cart_page.is_product_in_cart()

    cart_page.remove_product_from_cart()

    assert cart_page.is_product_removed()
