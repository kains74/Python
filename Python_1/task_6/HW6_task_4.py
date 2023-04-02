__author__ = "Василенко Сергей Александрович"

# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

import keyboard, time
class Car:
    speed = 0
    color = None
    name = None
    is_police = [True, False]


    def run(self):
        while True:
            if keyboard.is_pressed('Up'):
                self.go()
                if keyboard.is_pressed('Left') or keyboard.is_pressed('Right'):
                    self.turn()
            elif keyboard.is_pressed('Esc'):
                break
            elif keyboard.is_pressed('Down'):
                self.stop()
                if keyboard.is_pressed('Left') or keyboard.is_pressed('Right'):
                    self.turn()
            else:
                if keyboard.is_pressed('Left') or keyboard.is_pressed('Right'):
                    self.turn()
                time.sleep(1 - time.time() % 1)
                if self.speed > 0:
                    self.speed -= 3
                    self.show_speed()
                else:
                    print(f"{self.name} стоит!")

    def go(self):
        if self.speed < 160:
            self.speed += 6
        self.show_speed()
        time.sleep(1 - time.time() % 1)

    def stop(self):
        if self.speed > 0:
            self.speed -= 16
            time.sleep(1 - time.time() % 1)
            self.show_speed()
        else:
            print(f"{self.name} стоит!")

    def turn(self):
        if keyboard.is_pressed('Left'):
            print("Машина поворачивает на лево!!!")
        elif keyboard.is_pressed('Right'):
            print("Машина поворачивает на право!!!")
    def show_speed(self):
        print(f"Ваша скорость : {self.speed}")

class TownCar(Car):
    color = 'Red'
    is_police = False
    name = 'Mazda'


    def show_speed(self):
        if self.speed > 60:
            print(f"Ваша скорость превышает ограничения, сбавте скорость!!! {self.speed}")
        else:
            print(self.speed)


class SportCar(Car):
    color = 'Green'
    is_police = False
    name = 'Alpha Tauri'
class WorkCar(Car):
    color = 'Blue'
    is_police = False
    name = 'Bus'

    def show_speed(self):
        if self.speed > 40:
            print(f"Ваша скорость превышает ограничения, сбавте скорость!!! {self.speed}")
        else:
            print(self.speed)



class PoliceCar(Car):
    color = "Black"
    is_police = True
    name = "Hyundai Santa Fe"




x = WorkCar()
x.run()
