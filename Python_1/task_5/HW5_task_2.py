__author__ = "Василенко Сергей Александрович"

# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

file = open("Hello World.txt", "r")
x = [y for y in file]
print(f"Колличество строк : {len(x)}")
i = 0
all_a = []
for a in x:
    i += 1
    len_a = len(a)
    if len_a > 2:
        y = a.split(" ")
        print(f"в строке № {i} строке {len(y)} слов")
        all_a.extend(y)
    elif a[0] == " ":
        print(f"в {i} строке нет слово")
    else:
        y = a
        print(f"в {i} строке 1 слово")
        all_a.append(y)
print(f"Всего слов в тексте {len(all_a)}")
file.close()
