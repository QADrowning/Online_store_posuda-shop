import time

import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.buy_product_page_posuda import Buy_product_page
from pages.login_page_posuda import Login_page
from pages.ordering_page_posuda import Ordering_page
from pages.product_choice_page_posuda import Product_choice_page

@pytest.mark.run(order=4)
def test_order_product():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    g = Service(executable_path='C:\\Users\\olgaa\\PycharmProjects\\Resourse\\chromedriver.exe')
    driver_g = webdriver.Chrome(options=options, service=g)

    print("Start test order product")

    login = Login_page(driver_g)
    login.autorization()

    time.sleep(7)

    cp = Product_choice_page(driver_g)
    cp.sorting_posuda()

    bp = Buy_product_page(driver_g)
    bp.buy_posuda()

    op = Ordering_page(driver_g)
    op.order_posuda()

    print("Complete test order product")