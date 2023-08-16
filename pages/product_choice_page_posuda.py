import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib3.util import url

from base.base_class import Base
from utilities.logger import Logger


class Product_choice_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # Locators
    posuda_category = "//*[@id='mCSB_1_container']/div/ul/li[7]/a"
    material_filter = "//*[@id='right_block_ajax']/div[1]/div[2]/div/div/form/div[2]/div[4]/div[1]/div"
    sub_filter_1 = "//span[@title='African Wood 2']"
    sub_filter_2 = "//span[@title='Green Banana Leaf']"
    sorting_button = "//*[@id='right_block_ajax']/div[1]/div[1]/div[2]/div/div[1]"
    sub_sorting = "//*[@id='right_block_ajax']/div[1]/div[1]/div[2]/div/div[2]/div/div[7]/span"
    main_word = "//*[@id='right_block_ajax']/div[1]/div[2]/div/div/form/div[2]/div[4]/div[1]"

     # Getters

    def get_posuda_category(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.posuda_category)))

    def get_material_filter(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.material_filter)))

    def get_sub_filter_1(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.sub_filter_1)))

    def get_sub_filter_2(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.sub_filter_2)))

    def get_sorting_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.sorting_button)))

    def get_sub_sorting(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.sub_sorting)))

    def get_main_word(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def click_posuda_category(self):
        time.sleep(5)
        self.get_posuda_category().click()
        print("Click category")

    def click_material_filter(self):
        self.get_material_filter().click()
        print("Click material filter")

    def click_sub_filter_1(self):
        self.get_sub_filter_1().click()
        print("Click sub filter 1")

    def click_sub_filter_2(self):
        self.get_sub_filter_2().click()
        print("Click sub filter 2")

    def click_sorting_button(self):
        self.get_sorting_button().click()
        print("Click sorting button")

    def click_sub_sorting(self):
        self.get_sub_sorting().click()
        print("Click subsort")

    # Methods

    def sorting_posuda(self):
        Logger.add_start_step(method="sorting_posuda")
        self.get_current_url()
        self.click_posuda_category()
        time.sleep(5)
        self.click_material_filter()
        self.click_sub_filter_1()
        self.click_sub_filter_2()
        self.click_sorting_button()
        self.click_sub_sorting()
        self.screenshot()
        Logger.add_end_step(url=self.driver_g.current_url, method="sorting_posuda")