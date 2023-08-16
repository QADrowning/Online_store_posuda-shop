import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib3.util import url

from base.base_class import Base
from utilities.logger import Logger


class Login_page(Base):

    url = 'https://posuda-shop.ru/'

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # Locators
    enter_button = "//div[@class='line-block__item no-shrinked']"
    user_email = "//input[@id='USER_LOGIN_POPUP']"
    password = "//input[@id='USER_PASSWORD_POPUP']"
    button_login = "//button[@name='Login1']"
    lk_button = "//*[@id=\"header\"]/div[1]/div/div/div[1]/div/div/div[3]/div/div/div/div/a"
    main_word = "//h1[@id='pagetitle']"

   # Getters

    def get_enter_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    def get_user_email(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_email)))

    def get_password(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_button_login(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))

    def get_lk_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.lk_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def click_enter_button(self):
        self.get_enter_button().click()
        print("Click enter button")

    def input_user_email(self, user_email):
        self.get_user_email().send_keys(user_email)
        print("Input user email")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_button_login(self):
        self.get_button_login().click()
        print("Click login button")

    def click_lk_button(self):
        self.get_lk_button().click()
        print("Click lk button")

    # Methods

    def autorization(self):
        Logger.add_start_step(method="autorization")
        self.driver_g.get(self.url)
        self.driver_g.maximize_window()
        self.get_current_url()
        time.sleep(7)
        self.click_enter_button()
        self.input_user_email("olga.a.sidorenko@mail.ru")
        self.input_password("uganda31")
        self.click_button_login()
        time.sleep(7)
        self.click_lk_button()
        self.assert_word(self.get_main_word(), 'Личный кабинет')
        Logger.add_end_step(url=self.driver_g.current_url, method="autorization")