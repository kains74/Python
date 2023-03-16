__author__ = "Василенко Сергей Александрович"

# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32


users = open("task_3.txt", "r", encoding='utf8')
x = [y.replace("\n", "").split(" ") for y in users]
tmp = {z: y for z, y in x if float(y) < 20000}
tmp2 = {z: float(y) for z, y in x}
tmp3 = sum(tmp2.values()) / len(tmp2.values())
print(f"Имеют доход меньше 20 000 {tmp}")
print(f"Средняя величина дохода сотрудников составляет :{tmp3: .2f}")
users.close()
