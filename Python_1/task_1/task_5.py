__author__ = "Василенко Сергей Александрович"

# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.

gain = int(input("Введите прибыль фирмы : "))
loss = int(input("Введите потери фирмы : "))
s = gain - loss
if s > 0:
    print("прибыль — выручка больше издержек")
elif s == 0:
    print("стагнация - фирма отработала в ноль")
else:
    print("убыток — издержки больше выручки")
