__author__ = "Василенко Сергей Александрович"

# 6. Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

gain = int(input("Введите вырочку фирмы : "))
loss = int(input("Введите потери фирмы : "))
s = gain - loss
if s > 0:
    rent = gain / loss
    staff = int(input("Введите число сотрудников : "))
    s_staff = s / staff
    print(f"Прибыль — выручка больше издержек. Прибыль на одного сотрудника {s_staff:.2f}")
elif s == 0:
    print("Стагнация - фирма отработала в ноль")
else:
    print("Убыток — издержки больше выручки")
