# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def power(number_one, number_two):
    if number_two == 0:
        return 1
    elif number_two > 0:
        return number_one * power(number_one, number_two - 1)
    else:
        return 1 / number_one * power(number_one, number_two + 1)
    
number_one = int(input("Введите число: "))
number_two = int(input("Введите целую степень: "))

print(power(number_one, number_two))