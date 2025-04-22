import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class OpenCartPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_home_page(self):
        self.driver.get('https://demo.opencart.com/')
        time.sleep(1.5)

    def click_element(self, by, locator):
        element = self.driver.find_element(by, locator)
        element.click()
        time.sleep(1.5)

    def input_text(self, by, locator, text):
        element = self.driver.find_element(by, locator)
        element.send_keys(text)
        time.sleep(0.5)

    def select_option_by_value(self, by, locator, value):
        element = self.driver.find_element(by, locator)
        element.click()
        time.sleep(0.5)
        option = self.driver.find_element(By.XPATH, f"//option[@value='{value}']")
        option.click()
        time.sleep(0.5)

    def back(self):
        self.driver.back()
        time.sleep(1.5)

def main():
    firefox_option = webdriver.FirefoxOptions()
    firefox_option.add_argument('--start-maximized')
    browser = webdriver.Firefox(options=firefox_option)

    page = OpenCartPage(browser)

    page.navigate_to_home_page()

    page.click_element(By.XPATH, "//div[@id='slideshow0']")

    page.click_element(By.XPATH, "//li[2]//a[1]//img[1]")

    page.click_element(By.XPATH, "//button[@title='Next (Right arrow key)']")

    page.click_element(By.XPATH, "//button[@title='Next (Right arrow key)']")
    page.back()
    actions = webdriver.ActionChains(browser)
    PC = browser.find_element(By.XPATH,"//a[@class='dropdown-toggle'][contains(text(),'Компьютеры')]")
    actions.move_to_element(PC).perform()
    page.click_element(By.XPATH, "//a[normalize-space()='PC (0)']")
    page.back()

    page.click_element(By.XPATH, "//a[@title='Личный кабинет']")
    page.click_element(By.XPATH, "//ul[@class='dropdown-menu dropdown-menu-right']//a[contains(text(),'Регистрация')]")

    page.input_text(By.XPATH, "//input[@id='register_email']", "katetest1@yandex.ru")
    page.input_text(By.XPATH, "//input[@id='register_password']", "Rgtj456704")
    page.input_text(By.XPATH, "//input[@id='register_confirm_password']", "Rgtj456704")
    page.input_text(By.XPATH, "//input[@id='register_firstname']", "Ekaterina")
    page.input_text(By.XPATH, "//input[@id='register_lastname']", "Polozhentseva")
    page.input_text(By.XPATH, "//input[@id='register_telephone']", "79779368202")
    page.select_option_by_value(By.XPATH, "//select[@id='register_country_id']", "176")
    page.select_option_by_value(By.XPATH, "//select[@id='register_zone_id']", "83")
    page.input_text(By.XPATH, "//input[@id='register_city']", "Москва")
    page.input_text(By.XPATH, "//input[@id='register_postcode']", "14422")
    page.input_text(By.XPATH, "//input[@id='register_address_1']", "ВДНХ")

    page.click_element(By.XPATH, "//a[@id='simpleregister_button_confirm']")

    page.input_text(By.XPATH, "//input[@placeholder='Поиск']", "htc")
    page.click_element(By.XPATH, "//button[@class='btn btn-default btn-lg']")

    page.click_element(By.XPATH, "//a[normalize-space()='HTC Touch HD']")

    page.click_element(By.XPATH, "//button[@id='button-cart']")

    page.click_element(By.XPATH, "//a[contains(text(),'Камеры')]")
    page.click_element(By.XPATH, "//a[normalize-space()='Canon EOS 5D']")

    page.click_element(By.XPATH, "//select[@id='input-option226']")
    page.click_element(By.XPATH, "//option[@value='15']")
    page.click_element(By.XPATH, "//button[@id='button-cart']")

    page.click_element(By.XPATH, "//a[contains(text(),'Планшеты')]")
    page.click_element(By.XPATH, "//a[normalize-space()='Samsung Galaxy Tab 10.1']")

    page.click_element(By.XPATH, "//button[@id='button-cart']")

    page.click_element(By.XPATH, "//a[contains(text(),'Отзывов (0)')]")

    page.input_text(By.XPATH, "//input[@id='input-name']", "Ekaterina")
    page.input_text(By.XPATH, "//textarea[@id='input-review']", "Ужасный планшет, 10 из 10")
    page.click_element(By.XPATH, "//input[@value='5']")
    page.click_element(By.XPATH, "//button[@id='button-review']")

    input("Press Enter to exit")
    browser.quit()

if __name__ == "__main__":
    main()