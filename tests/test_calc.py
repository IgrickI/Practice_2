import pytest

from calculator.calc import add, sub, mul, div, mod, calculate, parse_expression


def test_add():
    """Проверка сложения"""
    assert add(2, 3) == 5


def test_sub():
    """Проверка вычитания"""
    assert sub(10, 4) == 6


def test_mul():
    """Проверка умножения"""
    assert mul(3, 4) == 12


def test_div():
    """Проверка деления"""
    assert div(10, 2) == 5

def test_mod():
    """Проверка остатка от деления"""
    assert mod(10, 2) == 0


def test_div_by_zero():
    """Проверка обработки деления на 0"""
    with pytest.raises(ZeroDivisionError):
        div(1, 0)


def test_parse_expression():
    """Проверка корректного парсинга"""
    assert parse_expression("2 + 3") == (2.0, "+", 3.0)


def test_calculate():
    """Полная проверка"""
    assert calculate("2 + 3") == 5
    assert calculate("10 * 4") == 40