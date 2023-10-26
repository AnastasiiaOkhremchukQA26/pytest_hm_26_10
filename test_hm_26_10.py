import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_mode', action='store', default="headless",
                     help="By default is headless mode, but you can set --browser_mode='gui'")

# Параметризована фікстура для старту та закриття браузера
@pytest.fixture
def browser(request):
    browser_mode = request.config.getoption("--browser_mode")
    if browser_mode == "gui":
        driver = webdriver.Chrome()
    elif browser_mode == "headless":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

# Перший тест
@pytest.mark.addition
def test_addition(browser):
    assert 1 + 1 == 2

# Другий тест
@pytest.mark.subtraction
def test_subtraction(browser):
    assert 3 - 1 == 2

# Третій тест
@pytest.mark.multiplication
def test_multiplication(browser):
    assert 2 * 3 == 6

# Четвертий тест
@pytest.mark.division
def test_division(browser):
    assert 6 / 2 == 3

# П'ятий тест
@pytest.mark.absolute
def test_absolute_value(browser):
    assert abs(-3) == 3
