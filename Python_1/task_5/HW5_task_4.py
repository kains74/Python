__author__ = "Василенко Сергей Александрович"

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

number_en = open("task_4.txt", "r", encoding='utf8')
x = [y.replace("\n", "").split(" — ") for y in number_en]
number_en.close()
eng = {z: int(y) for z, y in x}
rus = {"Один": 1, "Два": 2, "Три": 3, "Четыре": 4}
# temp_list = list(rus.items())
# print(temp_list[0])
number_rus = open("task_4_2.txt", "w")
for a in eng:
    for b in rus:
        if rus[b]  == eng[a]:
            print(f"{b} — {rus[b]}", file=number_rus)
number_rus.close()


