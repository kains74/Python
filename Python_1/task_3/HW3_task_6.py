__author__ = "Василенко Сергей Александрович"

# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func():
    text = input("Введите слово: ")
    print(text.title())

int_func()