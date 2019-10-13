"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
"""

number = input("Введите число")

if number.isdigit():
    number = int(number)
    summary = 0
    big_nun = 0
    while number: # 0 is False любое логическое действие с 0 дает False
        if number % 10 > big_nun:
            big_nun = number % 10
        summary += number % 10 # отделяем последнюю цифру от числа и увеличиваем сумму на это число
        number //= 10 # переопределяем number приравнивая его к целочисленному при делении на 10
    print(f"сумма равна: {summary}")
    print(f"Самая большая цифра {big_nun}")

else:
    print("Введено не число")
