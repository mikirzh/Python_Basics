"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def division(a: float) -> float:
    """
    делит a на b
    :param a:
    :param b:
    :return: float or None
    """
    try:
        return a / b
    expert ZeroDivisionError as e:
        print('Нельзя делить на ноль')

 division2 = lambda a, b: a / b if b else None



assert division(4, 2) == 2, 'division(4, 2)'
assert division(14, 2) == 7, 'division(14, 2)'
assert division(0, 2) == 0, 'division(0, 2)'
assert division(-22, 4) == -5.5, 'division(-22, 4)'
assert division(1, 0) is None, 'division(1, 0)'

assert division2(4, 2) == 2, 'division2(4, 2)'
assert division2(14, 2) == 7, 'division2(14, 2)'
assert division2(0, 2) == 0, 'division2(0, 2)'
assert division2(-22, 4) == -5.5, 'division2(-22, 4)'
assert division2(1, 0) is None, 'division2(1, 0)'