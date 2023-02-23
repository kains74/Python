gain = int(input("Введите вырочку фирмы : "))
loss = int(input("Введите потери фирмы : "))
s = gain - loss
if s > 0:
    rent = gain / loss
    staff = int(input("Введите число сотрудников : "))
    s_staff = s / staff
    print(f"прибыль — выручка больше издержек. Прибыль на одного сотрудника {s_staff:.2f}")
elif s == 0:
    print("стагнация - фирма отработала в ноль")
else:
    print("убыток — издержки больше выручки")
