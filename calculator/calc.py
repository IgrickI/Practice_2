def add(a: float, b: float) -> float:
    """Возвращает сумму двух чисел"""
    return a + b


def sub(a: float, b: float) -> float:
    """Возвращает разность двух чисел"""
    return a - b


def mul(a: float, b: float) -> float:
    """Возвращает произведение двух чисел"""
    return a * b


def div(a: float, b: float) -> float:
    """Возвращает частное. Бросает ZeroDivisionError при b == 0"""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль")
    return a / b


def mod(a: float, b: float) -> float:
    """Возвращает остаток от деления числе"""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль")
    return a % b


OPERATIONS = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    "%": div,
}


def parse_expression(expression: str) -> tuple[float, str, float]:
    """Разбирает строку вычисления на (левое, оператор, правое)"""
    parts = expression.split()
    if len(parts) != 3:
        raise ValueError("Ожидается формат: число оператор число")
    left, operator, right = parts
    if operator not in OPERATIONS:
        raise ValueError(f"Неизвестный оператор: {operator}")
    return float(left), operator, float(right)


def calculate(expression: str) -> float:
    """Вычисляет результат выражения"""
    a, operator, b = parse_expression(expression)
    return OPERATIONS[operator](a, b)


def main() -> None:
    """Читает выражение из stdin и печатает результат"""
    expression = input("Введите выражение (например, 2 + 3): ")
    try:
        print(f"Результат: {calculate(expression)}")
    except (ValueError, ZeroDivisionError) as exc:
        print(f"Ошибка: {exc}")


if __name__ == "__main__":
    main()