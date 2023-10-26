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
