__author__ = "Василенко Сергей Александрович"

#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    x = [a, b, c]
    x.sort(reverse=True)
    return print(x[0]+x[1])

my_func(99, 12, 45)