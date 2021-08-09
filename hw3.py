"""
Подается одна строка на вход и разбивается на элементы списка, считая пробел символом разделителя
Создаем словарь, где ключи это элементы списка. Если ключ повторяется, то значение в словаре по
ключу увеличивается на 1. Находим максимальное значение в словаре и ищем ключи, у которых значение равно максимальному
"""


def searchOftenMeetsWord():
    seq = input("Enter  sequence: ").lower().split()  # Преобразование строки в список
    if not seq:  # проверка наполнения строки
        exit()  # выход в случае пустой строки
    else:
        dic = dict()
        for i in seq:  # Наполнение словаря
            if i not in dic.keys():
                dic[i] = 1
            else:
                dic[i] += 1
        count = max(dic.values())  # Находим максимальное значение в словаре
        for key in dic.keys():  # Ищем ключи, значение по которым равно максимальному значению в словаре
            if dic[key] == count:
                print(f"{count} - {key}")
        searchOftenMeetsWord()


searchOftenMeetsWord()
