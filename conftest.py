import pytest


@pytest.fixture() #для одного теста
def set_up():
    print("Привет")
    yield
    print("Пока")

@pytest.fixture(scope="module") #для всех тестов
def set_group():
    print("Enter system")
    yield
    print("Exit system")

    # set_group,set_up - сначала всё, что в set_group до yield, потом для каждого теста set_up, заканчивается Exit system
    