# Задача 28: Напишите рекурсивную функцию find_sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def find_sum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return find_sum(a - 1, b + 1)

number_one = int(input("Введите первое число: "))
number_two = int(input("Введите второе число: "))

print(find_sum(number_one, number_two))