time = int(input("Введите время в секундах: "))
mm_temp = time // 60
hh = mm_temp // 60
mm = mm_temp % 60
cc = time - (((hh * 60) + mm) * 60)
print(f"{hh}:{mm}:{cc}")
