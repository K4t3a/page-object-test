import time
import random
import string
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

# Инициализация Faker для генерации случайных данных
fake = Faker('ru_RU')

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Ожидание до 10 секунд

    def click_element(self, by, locator):
        """Клик по элементу"""
        element = self.wait.until(EC.element_to_be_clickable((by, locator)))
        element.click()
        time.sleep(0.5)

    def input_text(self, by, locator, text):
        """Ввод текста в поле"""
        element = self.wait.until(EC.presence_of_element_located((by, locator)))
        element.clear()
        element.send_keys(text)
        time.sleep(0.5)

    def select_option_by_value(self, by, locator, value):
        """Выбор опции в выпадающем списке по значению"""
        element = self.wait.until(EC.element_to_be_clickable((by, locator)))
        element.click()
        option = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//option[@value='{value}']")))
        option.click()
        time.sleep(0.5)

    def hover_element(self, by, locator):
        """Наведение курсора на элемент"""
        element = self.wait.until(EC.element_to_be_clickable((by, locator)))
        ActionChains(self.driver).move_to_element(element).perform()
        time.sleep(0.5)

    def back(self):
        """Возврат на предыдущую страницу"""
        self.driver.back()
        time.sleep(1)

class HomePage(BasePage):
    def navigate(self):
        """Переход на главную страницу"""
        self.driver.get('https://demo.opencart.com/')
        time.sleep(1)

    def click_slideshow(self):
        """Клик по слайдшоу"""
        self.click_element(By.XPATH, "//div[@id='slideshow0']")

    def click_second_banner(self):
        """Клик по второму баннеру"""
        self.click_element(By.XPATH, "//li[2]//a[1]//img[1]")

    def click_next_button(self):
        """Клик по кнопке 'Далее' в слайдшоу"""
        self.click_element(By.XPATH, "//button[@title='Next (Right arrow key)']")

    def hover_desktops(self):
        """Наведение на категорию 'Desktops'"""
        self.hover_element(By.XPATH, "//a[@class='dropdown-toggle'][contains(text(),'Desktops')]")

    def click_pc_category(self):
        """Клик по категории 'PC'"""
        self.click_element(By.XPATH, "//a[normalize-space()='PC (0)']")

    def click_my_account(self):
        """Клик по 'Мой аккаунт'"""
        self.click_element(By.XPATH, "//a[@title='My Account']")

    def click_register(self):
        """Клик по пункту 'Регистрация'"""
        self.click_element(By.XPATH, "//ul[@class='dropdown-menu dropdown-menu-right']//a[contains(text(),'Register')]")

    def search_product(self, product_name):
        """Поиск товара по названию"""
        self.input_text(By.XPATH, "//input[@placeholder='Search']", product_name)
        self.click_element(By.XPATH, "//button[@class='btn btn-default btn-lg']")

class RegisterPage(BasePage):
    def fill_registration_form(self, email, password, first_name, last_name, telephone, country_id, zone_id, city, postcode, address):
        """Заполнение формы регистрации"""
        self.input_text(By.XPATH, "//input[@id='register_email']", email)
        self.input_text(By.XPATH, "//input[@id='register_password']", password)
        self.input_text(By.XPATH, "//input[@id='register_confirm_password']", password)
        self.input_text(By.XPATH, "//input[@id='register_firstname']", first_name)
        self.input_text(By.XPATH, "//input[@id='register_lastname']", last_name)
        self.input_text(By.XPATH, "//input[@id='register_telephone']", telephone)
        self.select_option_by_value(By.XPATH, "//select[@id='register_country_id']", country_id)
        self.select_option_by_value(By.XPATH, "//select[@id='register_zone_id']", zone_id)
        self.input_text(By.XPATH, "//input[@id='register_city']", city)
        self.input_text(By.XPATH, "//input[@id='register_postcode']", postcode)
        self.input_text(By.XPATH, "//input[@id='register_address_1']", address)
        self.click_element(By.XPATH, "//a[@id='simpleregister_button_confirm']")

class ProductPage(BasePage):
    def add_to_cart(self):
        """Добавление товара в корзину"""
        self.click_element(By.XPATH, "//button[@id='button-cart']")

    def select_option(self, option_id):
        """Выбор опции товара"""
        self.click_element(By.XPATH, f"//select[@id='input-option{option_id}']")
        self.click_element(By.XPATH, "//option[@value='15']")

    def add_to_wishlist(self):
        """Добавление товара в вишлист"""
        self.click_element(By.XPATH, "//button[@data-original-title='Add to Wish List']")

    def click_reviews_tab(self):
        """Переход на вкладку отзывов"""
        self.click_element(By.XPATH, "//a[contains(text(),'Reviews (0)')]")

    def write_review(self, name, review_text, rating):
        """Написание отзыва о товаре"""
        self.input_text(By.XPATH, "//input[@id='input-name']", name)
        self.input_text(By.XPATH, "//textarea[@id='input-review']", review_text)
        self.click_element(By.XPATH, f"//input[@value='{rating}']")
        self.click_element(By.XPATH, "//button[@id='button-review']")

class CartPage(BasePage):
    def view_cart(self):
        """Просмотр корзины"""
        self.click_element(By.XPATH, "//a[@title='Shopping Cart']")

class TestOpenCart:
    def __init__(self, browser_type):
        """Инициализация браузера"""
        if browser_type.lower() == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument('--start-maximized')
            self.driver = webdriver.Chrome(options=options)
        elif browser_type.lower() == 'firefox':
            options = webdriver.FirefoxOptions()
            options.add_argument('--start-maximized')
            self.driver = webdriver.Firefox(options=options)
        else:
            raise ValueError("Неподдерживаемый браузер! Используйте 'chrome' или 'firefox'")

    def generate_random_password(self, length=10):
        """Генерация случайного пароля"""
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    def run_tests(self):
        """Запуск всех тестов"""
        try:
            home_page = HomePage(self.driver)
            register_page = RegisterPage(self.driver)
            product_page = ProductPage(self.driver)
            cart_page = CartPage(self.driver)

            # Генерация случайных данных для тестов
            email = fake.email()
            password = self.generate_random_password()
            first_name = fake.first_name()
            last_name = fake.last_name()
            telephone = fake.phone_number()
            city = fake.city()
            postcode = fake.postcode()
            address = fake.street_address()

            # Тест 1: Переход и взаимодействие с главной страницей
            home_page.navigate()
            home_page.click_slideshow()

            # Тест 2: Взаимодействие с баннерами
            home_page.click_second_banner()
            home_page.click_next_button()
            home_page.click_next_button()
            home_page.back()

            # Тест 3: Переход в категорию PC
            home_page.hover_desktops()
            home_page.click_pc_category()
            home_page.back()

            # Тест 4: Регистрация нового пользователя
            home_page.click_my_account()
            home_page.click_register()
            register_page.fill_registration_form(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                telephone=telephone,
                country_id="176",  # Россия
                zone_id="83",     # Москва
                city=city,
                postcode=postcode,
                address=address
            )

            # Тест 5: Поиск и просмотр товара
            home_page.search_product("iphone")

            # Тест 6: Добавление телефона HTC в корзину
            home_page.search_product("htc")
            home_page.click_element(By.XPATH, "//a[normalize-space()='HTC Touch HD']")
            product_page.add_to_cart()

            # Тест 7: Добавление камеры в корзину
            home_page.click_element(By.XPATH, "//a[contains(text(),'Cameras')]")
            home_page.click_element(By.XPATH, "//a[normalize-space()='Canon EOS 5D']")
            product_page.select_option("226")
            product_page.add_to_cart()

            # Тест 8: Добавление планшета в корзину
            home_page.click_element(By.XPATH, "//a[contains(text(),'Tablets')]")
            home_page.click_element(By.XPATH, "//a[normalize-space()='Samsung Galaxy Tab 10.1']")
            product_page.add_to_cart()

            # Тест 9: Добавление товара в вишлист
            home_page.search_product("iphone")
            home_page.click_element(By.XPATH, "//a[normalize-space()='iPhone']")
            product_page.add_to_wishlist()

            # Тест 10: Написание отзыва о товаре
            home_page.click_element(By.XPATH, "//a[contains(text(),'Tablets')]")
            home_page.click_element(By.XPATH, "//a[normalize-space()='Samsung Galaxy Tab 10.1']")
            product_page.click_reviews_tab()
            product_page.write_review(
                name=first_name,
                review_text=f"Отличный товар, рекомендую! {fake.sentence()}",
                rating=str(random.randint(3, 5))  # Случайный рейтинг от 3 до 5
            )

            input("Нажмите Enter для завершения")
        finally:
            self.driver.quit()

def main():
    """Запуск тестов в Chrome и Firefox"""
    # Тесты в Chrome
    chrome_tests = TestOpenCart('chrome')
    chrome_tests.run_tests()

    # Тесты в Firefox
    firefox_tests = TestOpenCart('firefox')
    firefox_tests.run_tests()

if __name__ == "__main__":
    main()