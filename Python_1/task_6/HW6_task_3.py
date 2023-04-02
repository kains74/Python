__author__ = "Василенко Сергей Александрович"

# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    name = None
    surname = None
    position = None
    _income = {"wage": 30000, "bonus": 10000}

class Position(Worker):
    def works(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self.get_full_name = name + " " + surname
        self.get_total_income = sum(Worker._income.values())

x = Position()
x.works("Кудрявцев", "Антон", "Баристо")
print(f"{x.get_full_name} - {x.get_total_income}")
