__author__ = "Василенко Сергей Александрович"

import numpy
# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
#
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
#
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.



class Matrix():
 #   numpy.matrix([[[1, 2, 3], [1, 2, 3], [1, 2, 3]]])
 #   def __str__(self):


    def __init__(self, x, y ,z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, d1):
        a = [tmp + tmp1 for tmp, tmp1 in zip(self.x, d1.x)]
        b = [tmp + tmp1 for tmp, tmp1 in zip(self.y, d1.y)]
        c = [tmp + tmp1 for tmp, tmp1 in zip(self.z, d1.z)]
        return Matrix(a, b, c)
    def __str__(self):
        return f"{self.x}\n{self.y}\n{self.z}\n"


a = [1, 2, 3]
b = [1, 2, 3]
c = [1, 2, 3]

a1 = [3, 2, 1]
b1 = [3, 2, 1]
c1 = [3, 2, 1]
d = Matrix(a, b, c)
d1 = Matrix(a1, b1, c1)
d_sum = d + d1
print(d)
print(d1)
print(d_sum)

