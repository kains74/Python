
while True:
    a = int(input("Введите пройденную дистанции : "))
    if a > 0:
        break
    else:
        print("Дистанция не может быть отрицательной!")
while True:
    b = int(input("Введите желаемое значение дистанции : "))
    if b > 0:
        break
    else:
        print("Дистанция не может быть отрицательной!")
i = 1
while True:
    print(f"{i}-й день: {a:.3f}")
    if a >= b:
        print(f"Ответ: на {i}-й день достигните результата - не менее {b} км")
        break
    i = i + 1
    a = a + a * 0.1

