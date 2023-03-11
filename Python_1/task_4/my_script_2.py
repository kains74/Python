from itertools import count, cycle

def int1(a):
    for i in count(a, 1):
        if i > 10:
            break
        else:
            print(i)

def int2(a, b):
    i = 0
    for i in cycle(a):
        if i > b:
            break
        else:
            print(i)
