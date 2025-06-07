from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def setup_driver(browser_name):
    if browser_name.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser_name.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser: use 'chrome' or 'firefox'")
    driver.maximize_window()
    return driver

def test_6_add_to_wishlist(pages, browser_name="chrome"):
    home_page, product_page, _, _, _ = pages
    driver = setup_driver(browser_name)
    home_page.set_driver(driver)
    
    home_page.scroll_down(400)
    time.sleep(2)
    product_page.select_prod("MacBook")
    time.sleep(2)
    product_page.add_to_wishlist()
    time.sleep(1)
    
    success_alert = home_page.driver.find_elements(By.CSS_SELECTOR, ".alert.alert-success")
    assert "Success: You have added" in success_alert[0].text, "Failed to add MacBook to wishlist"
    
    time.sleep(2)
    home_page.click_logo()
    driver.quit()

def test_7_add_camera_to_cart(pages, browser_name="chrome"):
    home_page, product_page, _, _, _ = pages
    driver = setup_driver(browser_name)
    home_page.set_driver(driver)
    
    home_page.click_catalog("camera")
    time.sleep(1)
    home_page.scroll_down(300)
    time.sleep(2)
    home_page.add_to_cart("Nikon D300")
    time.sleep(1)
    
    success_alert = home_page.driver.find_elements(By.CSS_SELECTOR, ".alert.alert-success")
    assert "Success: You have added" in success_alert[0].text, "Failed to add Nikon D300 to cart"
    
    time.sleep(2)
    home_page.scroll_up(0)
    driver.quit()

def test_8_add_tablet_to_cart(pages, browser_name="chrome"):
    home_page, _, _, _, _ = pages
    driver = setup_driver(browser_name)
    home_page.set_driver(driver)
    
    home_page.click_catalog("tablet")
    time.sleep(1)
    home_page.scroll_down(200)
    time.sleep(2)
    home_page.add_to_cart("Samsung Galaxy Tab 10.1")
    time.sleep(1)
    
    success_alert = home_page.driver.find_elements(By.CSS_SELECTOR, ".alert.alert-success")
    assert "Success: You have added" in success_alert[0].text, "Failed to add Samsung Galaxy Tab to cart"
    
    time.sleep(2)
    home_page.scroll_up(0)
    driver.quit()

def test_9_add_htc_to_cart(pages, browser_name="chrome"):
    home_page, _, _, _, _ = pages
    driver = setup_driver(browser_name)
    home_page.set_driver(driver)
    
    home_page.click_catalog("smartphone")
    time.sleep(1)
    home_page.scroll_down(300)
    time.sleep(2)
    home_page.add_to_cart("HTC Touch HD")
    time.sleep(1)
    
    success_alert = home_page.driver.find_elements(By.CSS_SELECTOR, ".alert.alert-success")
    assert "Success: You have added" in success_alert[0].text, "Failed to add HTC Touch HD to cart"
    
    time.sleep(2)
    home_page.scroll_up(0)
    driver.quit()

def test_10_write_review(pages, browser_name="chrome"):
    home_page, product_page, review_page, _, _ = pages
    driver = setup_driver(browser_name)
    home_page.set_driver(driver)
    
    home_page.click_catalog("laptop")
    time.sleep(1)
    product_page.select_prod("HP LP3065")
    home_page.scroll_down(600)
    time.sleep(2)
    review_page.click_review()
    home_page.scroll_down(900)
    time.sleep(2)
    review_page.input_review("Test Review", "Great product!", 5)
    time.sleep(1)
    
    success_alert = home_page.driver.find_elements(By.CSS_SELECTOR, ".alert.alert-success")
    assert "Thank you for your review" in success_alert[0].text, "Failed to submit review for HP LP3065"
    
    time.sleep(2)
    home_page.scroll_up(0)
    driver.quit()
