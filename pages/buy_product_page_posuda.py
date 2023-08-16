import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib3.util import url

from base.base_class import Base
from utilities.logger import Logger


class Buy_product_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # Locators
    product_1 = "//*[@id='bx_3966226736_44851']/div/div[1]/a/span/span"
    product_2 = "//*[@id='bx_3966226736_44835']/div"
    price_product_1 = "//*[@id='bx_117848907_44851']/div/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div[1]/div/div"
    price_product_2 = "//*[@id='bx_117848907_44835']/div/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div[1]/div/div"
    add_to_cart_product_1 = "//*[@id='bx_117848907_44851_basket_actions']/span[1]"
    add_to_cart_product_2 = "//*[@id='bx_117848907_44835_basket_actions']/span[1]"
    cart_button = "//*[@id='header']/div[1]/div/div/div[2]/div/div[3]/div/div[3]/a"
    main_word = "//*[@id='pagetitle']"

     # Getters

    def get_product_1(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1)))

    def get_product_2(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_2)))

    def get_add_to_cart_product_1(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_product_1)))

    def get_add_to_cart_product_2(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_product_2)))

    def get_cart_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_price_product_1(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product_1)))

    def get_price_product_2(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product_2)))

    def get_main_word(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def click_product_1(self):
        self.driver_g.execute_script("window.scrollTo(0,750);")
        time.sleep(5)
        self.get_product_1().click()
        print("Open product 1")

    def click_add_to_cart_product_1(self):
        time.sleep(5)
        self.get_add_to_cart_product_1().click()
        print("Add to cart product 1")

    def click_product_2(self):
        self.driver_g.execute_script("window.scrollTo(0,1050);")
        time.sleep(5)
        self.get_product_2().click()
        print("Open product 2")

    def click_add_to_cart_product_2(self):
        self.get_add_to_cart_product_2().click()
        print("Add to cart product 2")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click cart button")

    def print_value_product_1(self):
        product_1 = self.driver_g.find_element(By.XPATH, "//*[@id='bx_3966226736_44851']/div")
        value_product_1 = product_1.text
        print("Выбранный товар 2: " + value_product_1)

    def print_value_product_2(self):
        product_2 = self.driver_g.find_element(By.XPATH, "//*[@id='bx_3966226736_44835']/div")
        value_product_2 = product_2.text
        print("Выбранный товар 2: " + value_product_2)

    # Methods

    def buy_posuda(self):
        Logger.add_start_step(method="buy_posuda")
        self.get_current_url()
        self.print_value_product_1()
        self.click_product_1()
        self.click_add_to_cart_product_1()
        self.driver_g.back()
        self.print_value_product_2()
        self.click_product_2()
        self.click_add_to_cart_product_2()
        self.click_cart_button()
        self.assert_word(self.get_main_word(), 'Корзина')
        self.screenshot()
        Logger.add_end_step(url=self.driver_g.current_url, method="buy_posuda")