__author__ = "Василенко Сергей Александрович"

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = None

    def draw(self):
        print("Запуск отрисовки")
        class Pen(Stationery):
            title = "Ручка"
            def draw(self):
                print(f"Это была {Pen.title}")

        a = Pen()
        a.draw()

        class Pencil(Stationery):
            title = "Карандашь"
            def draw(self):
                print(f"Это был {Pencil.title}")

        b = Pencil()
        b.draw()

        class Handle(Stationery):
            title = "Маркер"
            def draw(self):
                print(f"Это был {Handle.title}")

        c = Handle()
        c.draw()

x = Stationery()
x.draw()

