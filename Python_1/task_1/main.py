c="год"
cc="года"
ccc="лет"
name = input("Как вас зовут?: ")
print (f"Привет {name}!")
while True :
    year = int(input("Сколько вам лет?: "))
    if 0< year < 200 :
        break
    print("Вы меня обманываете!Скажите правду!")
if year > 200 :
    print("")
elif year >= 100 :
    print (f"{year} {ccc},ох,присаживайтесь пожалуйста!")
elif year >= 50 :
    print (f"{year} {ccc}, ещё пару десятков миниму прожить нужно!")
elif year >= 18 :
    print(f"всего {year} {ccc}, до пенсии ещё далеко,так что учись и учись!")
else:
    b = 0
    while True:
        year = year + 1
        b = b + 1
        if year == 18:
            break

    if b == 1:
        years = c
    elif 2<=b<=4 :
        years = cc
    else:
        years = ccc
    print(f"Ну ты совсем ещё маленьки,приходи хотя бы через {b} {years} ")
