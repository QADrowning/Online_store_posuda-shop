import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class Ordering_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # Locators
    product_1_in_cart = "//*[@id='basket-item-height-aligner-17011']"
    product_2_in_cart = "//*[@id='basket-item-height-aligner-17012']"
    price_product_1_in_cart = "//*[@id='basket-item-17011']/td[2]/div"
    price_product_2_in_cart = "//*[@id='basket-item-17012']/td[2]/div"
    ordering_button = "//*[@id='basket-root']/div[1]/div/div/div[2]/div/div[3]/div/div[1]/button"
    main_word = "//*[@id='pagetitle']"
    delivery = "//*[@id='bx-soa-delivery']/div[2]/div[2]/div/div[4]/div[1]"
    phone = "//input[@type='tel']"
    item_1 = "//*[@id='bx-soa-basket']/div[2]/div[1]/div/table/tr[2]/td[1]/div/div[2]/div/a"
    item_2 = "//*[@id='bx-soa-basket']/div[2]/div[1]/div/table/tr[3]/td[1]/div/div[2]/div/a"
    finish_button = "//*[@id='bx-soa-total']/div[2]/div[5]"

     # Getters

    def get_ordering_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.ordering_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_delivery(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery)))

    def get_phone(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_item_1(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_1)))

    def get_item_2(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_2)))

    def get_finish_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_button)))

    # Actions

    def click_ordering_button(self):
        self.get_ordering_button().click()
        print("Open ordering page")

    def click_delivery(self):
        self.get_delivery().click()
        self.driver_g.execute_script("window.scrollTo(0,1250);")
        time.sleep(5)
        print("Click delivery button")

    def click_phone(self):
        self.get_phone().click()
        print("Click phone field")

    def input_phone(self,phone):
        self.get_phone().send_keys(phone)
        self.driver_g.execute_script("window.scrollTo(0,1250);")
        print("Input phone")

    def print_product_1_in_cart(self):
        product_1 = self.driver_g.find_element(By.XPATH, "//*[@id='bx-soa-basket']/div[2]/div[1]/div/table/tr[2]/td[1]/div/div[2]/div/a")
        value_product_1 = product_1.text
        print("Товар 1 на итоговой странице: " + value_product_1)

    def print_price_product_1_in_cart(self):
        price_product_1 = self.driver_g.find_element(By.XPATH, "//*[@id='bx-soa-basket']/div[2]/div[1]/div/table/tr[2]/td[4]/div[2]/strong")
        value_price_product_1 = price_product_1.text
        print("Цена товара 2 на итоговой странице: " + value_price_product_1)

    def print_product_2_in_cart(self):
        product_2 = self.driver_g.find_element(By.XPATH, "//*[@id='bx-soa-basket']/div[2]/div[1]/div/table/tr[3]/td[1]/div/div[2]/div/a")
        value_product_2 = product_2.text
        print("Товар 2 на итоговой странице: " + value_product_2)

    def print_price_product_2_in_cart(self):
        price_product_2 = self.driver_g.find_element(By.XPATH, "//*[@id='bx-soa-basket']/div[2]/div[1]/div/table/tr[3]/td[4]/div[2]/strong")
        value_price_product_2 = price_product_2.text
        print("Цена товара 2 на итоговой странице: " + value_price_product_2)

    def click_finish_button(self):
        self.get_finish_button().click()
        print("Click finish button")

     # Methods

    def order_posuda(self):
        Logger.add_start_step(method="order_posuda")
        self.click_ordering_button()
        self.get_current_url()
        self.assert_word(self.get_main_word(), 'Оформление заказа')
        self.print_product_1_in_cart()
        self.print_price_product_1_in_cart()
        self.print_product_2_in_cart()
        self.print_price_product_2_in_cart()
        self.click_delivery()
        time.sleep(7)
        self.input_phone("9999999999")
        time.sleep(7)
        self.assert_word(self.get_item_1(), 'Салатник меламиновый 28.*28*8см, P.L. Аfrican wood 2')
        self.assert_word(self.get_item_2(), 'Блюдо (GN 2/4) меламин 53*16.2*6.5см P.L. Green Banana Leaf')
        # self.click_finish_button()
        self.screenshot()
        Logger.add_end_step(url=self.driver_g.current_url, method="order_posuda")