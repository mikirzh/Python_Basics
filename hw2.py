"""
Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""


# запрашиваем число у пользователя
user_number = input("введите число")

# проверим что введено число
if user_number.isdigit():
    # преобразуем строку в число
    user_number = int(user_number)
    result = user_number + int(str(user_number)*2) + int(str(user_number)*3)
    print(result)
else:
    print("Введено не число")