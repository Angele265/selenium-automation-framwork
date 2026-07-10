def test_home_page_title(driver):

    driver.get("https://automationexercise.com")

    assert driver.title == "Automation Exercise"


