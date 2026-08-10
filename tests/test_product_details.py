from pages.home_page import HomePage
from pages.products_page import ProductSearch
from pages.product_details_page import ProductDetailsPage


def test_view_product_details(driver):
    home_page = HomePage(driver)
    product_page = ProductSearch(driver)
    product_details_page = ProductDetailsPage(driver)



    home_page.open()
    product_page.click_products_button()
    product_page.search_products("Blue Top")

    product_page.submit_search()

    # Verify search returned products
    assert product_page.are_products_displayed()

    # Open product
    product_details_page.click_product_details()

    # Verify product details
    assert product_details_page.get_product_name() == "Blue Top"

    assert "Rs." in product_details_page.get_price()

    assert "Availability" in product_details_page.get_availability()

    assert "Condition" in product_details_page.get_condition()

    assert "Brand" in product_details_page.get_brand()

    assert "Category" in product_details_page.get_category()