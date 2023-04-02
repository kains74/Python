__author__ = "Василенко Сергей Александрович"

import time


# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.


class TrafficLight:
    __color = "red"

    @staticmethod
    def running():
        for a in range(7):
            time.sleep(1 - time.time() % 1)
            print(a, TrafficLight.__color)
        for b in range(2):
            TrafficLight.__color = "yellow"
            time.sleep(1 - time.time() % 1)
            print(b, TrafficLight.__color)
        for c in range(7):
            TrafficLight.__color = "green"
            time.sleep(1 - time.time() % 1)
            print(c, TrafficLight.__color)

x = TrafficLight()
x.running()
