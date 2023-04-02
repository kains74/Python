__author__ = "Василенко Сергей Александрович"

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

import random

file_w = open("task_5.txt", "w")
i = 0

while True:
    file_w.write(f"{random.randrange(1, 9)} ")
    i += 1
    if i == 10:
        break
file_w.close()
file_r = open("task_5.txt", "r")
x = [int(y) for y in file_r.readline().split(" ") if y != ""]
print(sum(x))
file_r.close()
