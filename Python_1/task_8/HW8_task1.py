__author__ = "Василенко Сергей Александрович"


# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

import datetime

class Date():
    def __init__(self, date):
        self.date = date.split("-")

    @classmethod
    def my_method1(cls, date):
        try:
            day, month, year = [int(y) for y in date.split("-")]
            datetime.datetime.strptime(date, '%d-%m-%Y')
            return f"{day}.{month}.{year}"
        except ValueError:
            return "Error"

    @staticmethod
    def my_method2(data):
        try:
            datetime.datetime.strptime(data, '%d-%m-%Y')
            return 'Есть такая дата!'
        except ValueError:
            return "Error"

print(Date.my_method1("12-12-1988"))
print(Date.my_method2("12-12-2188"))