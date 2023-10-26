import pytest
from selenium import webdriver


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
