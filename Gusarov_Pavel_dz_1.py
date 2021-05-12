"""
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
* до минуты: <s> сек;
* до часа: <m> мин <s> сек;
* до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""

# duration = int(input("Enter a number: "))
#
# if duration <= 59:
#     print(f"{duration} sec")
# elif 60 <= duration <= 3599:
#     m = duration // 60
#     s = duration % 60
#     print(f"{m} min {s} sec")
# elif 3600 <= duration <= 86399:
#     h = duration // 60 // 60
#     m = duration // 60 % 60
#     s = duration % 60
#     print(f"{h} hour {m} min {s} sec")
# elif 86400 <= duration:
#     d = duration // 60 // 60 // 24
#     h = duration // 60 // 60 % 24
#     m = duration // 60 % 60
#     s = duration % 60
#     print(f"{d} days {h} hour {m} min {s} sec")


"""
2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
сумма цифр которых делится нацело на 7. Внимание: новый список не создавать!!!
"""


def sum_digits(number):
    total = 0
    while number != 0:
        last_digit = number % 10
        total += last_digit
        number //= 10
    return total


"""
Решение без "+17"
"""
my_arr = []
sum_arr = 0

for num in range(1, 1001, 2):
    num = num ** 3
    result = sum_digits(num)
    if result % 7 == 0:
        my_arr.append(num)

for i in my_arr:
    sum_arr = sum_arr + i

print(f"Without 'plus 17': {my_arr}")
print(f"The sum of all elements in 'my_arr': {sum_arr}")


"""
Решение с "+17"
"""
my_arr = []

for num in range(1, 1001, 2):
    num = num ** 3
    result = sum_digits(num)
    if result % 7 == 0:
        num = num + 17
        result_x = sum_digits(num)
        if result_x % 7 == 0:
            my_arr.append(num)

print(f"With 'plus 17': {my_arr}")


"""
3. Реализовать склонение слова «процент» для чисел до 20.
Например, задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента».
Вывести все склонения для проверки.
"""

# user_number = int(input("Enter a number from 1 to 20: "))
#
# if user_number == 1:
#     last = ""
# elif 1 < user_number < 5:
#     last = "а"
# else:
#     last = 'ов'
#
# print(f"{user_number} процент{last}")