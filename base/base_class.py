import datetime

class Base():
    def __init__(self, driver_g):
        self.driver_g = driver_g

        ###Метод получения url

    def get_current_url(self):
        get_url=self.driver_g.current_url
        print("Current url " + get_url)

        ###Метод проверки текста

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Correct value")

    def assert_price_1(self, get_item_price_1, price_product_1):
        value_price_1 = get_item_price_1.text
        value_price_2 = price_product_1.text
        assert value_price_1 == value_price_2
        print("Correct price item 1")

    def assert_price_2(self, get_item_price_2, price_product_2):
        value_price_1 = get_item_price_2.text
        value_price_2 = price_product_2.text
        assert value_price_1 == value_price_2
        print("Correct price item 2")

        ###Метод скриншот

    def screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver_g.save_screenshot('C:\\Users\\olgaa\\PycharmProjects\\dishes\\screen\\' + name_screenshot)

        ###Метод assert url

    def assert_url(self, result):
        get_url = self.driver_g.current_url
        assert get_url == result
        print("Correct url")





