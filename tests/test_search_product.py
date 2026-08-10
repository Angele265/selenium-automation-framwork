from pages.products_page import ProductSearch
from pages.home_page import HomePage

def test_search_product(driver):
    home_page = HomePage(driver)
    product_page = ProductSearch(driver)

    home_page.open()
    product_page.click_products_button()
    product_page.search_products("Top")
    product_page.submit_search()
    assert product_page.are_products_displayed()
