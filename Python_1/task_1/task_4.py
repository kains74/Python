while True:
    n = int(input("Введите положительное число :"))
    if n >= 0:
        break
    print("Ошибка, введено отрицательное число!")
a = 0
while True:
    b = n % 10
    n = n // 10
    if n == 0:
        if b >= a:
            a = b
        break
    if b >= a:
        a = b
print(a)
