__author__ = "Василенко Сергей Александрович"

# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введён после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

x = int(0)
bb = []
def my_func():
    return sum(bb)

while True:
    aa = input("Введите значение: ").split( )
    for k in aa:
        if k == "!":
            print(my_func())
            exit()
        else:
            bb.append(int(k))

    print(my_func())
