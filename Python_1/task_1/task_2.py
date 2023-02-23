while True:
    time = int(input("Введите время в секундах: "))
    if time > 0:
        break
    print("Время не может быть отрицательным!")
mm_temp = time // 60
hh = mm_temp // 60
mm = mm_temp % 60
cc = time - (((hh * 60) + mm) * 60)
print(f"{hh}:{mm}:{cc}")
