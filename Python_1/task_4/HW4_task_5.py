__author__ = "Василенко Сергей Александрович"

# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

def my_func (a,b):
    return a + b

x = [reduce(my_func, (y for y in range(100, 1000+2, 2)))]
print(x)
