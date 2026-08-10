from pages.home_page import HomePage
from pages.products_page import ProductSearch
from pages.cart_page import CartPage

def test_add_to_cart(driver):
    home_page = HomePage(driver)
    product_page = ProductSearch(driver)
    cart_page = CartPage(driver)

    home_page.open()

    product_page.click_products_button()

    product_page.add_item_to_cart()

    home_page.click_cart()

    assert cart_page.get_product_name() == "Blue Top"

    assert cart_page.get_product_price() == "Rs. 500"

    assert cart_page.get_product_qtty() == "1"

    assert cart_page.get_product_total() == "Rs. 500"


