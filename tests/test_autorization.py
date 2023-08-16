import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page_posuda import Login_page

@pytest.mark.run(order=1)
def test_autorization():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    g = Service(executable_path='C:\\Users\\olgaa\\PycharmProjects\\Resourse\\chromedriver.exe')
    driver_g = webdriver.Chrome(options=options, service=g)

    print("Start test autorization")

    login = Login_page(driver_g)
    login.autorization()

    print("Complete test autorization")