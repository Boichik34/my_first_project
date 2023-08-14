import controller
import re
import os


def chek_book():
    os.system('cls||clear')
    print("------------------------------")
    book_name = input(f'''
Введите название книги,которую хотите добавить:
>>>''')
    file = open("text.txt", "r", encoding="utf8")
    lst = file.read()
    lst_1 = lst.split("\n")
    lst_2 = []
    file.close()
    for el in lst_1:
        a = el.split(",")
        lst_2.append(a[0])
    if book_name.title() in lst_2:
        os.system('cls||clear')
        print("-------------------------------")
        print("Книга, которую вы хотите добавить, уже есть в каталоге!")
        controller.print_commands()
    else:
        return book_name.title()


def get_catalog():
    file = open("text.txt", "r", encoding="utf8")
    catalog = file.read()
    file.close()
    if len(catalog) != 0:
        return catalog
    else:
        print("------------------------------")
        print("Каталог пуст!")
        controller.print_commands()


def check_date():
    data = input(f'''
Введите год издания:
>>>''')
    while not data.isdigit() or len(data) != 4 or int(data) > 2023:
        print("------------------------------")
        print("Некорректный ввод!")
        data = input(f'''
Введите год издания в формате '0000'
>>>''')
    return data


def get_name_del() -> str:
    name_del = input(f'''
Введите название книги которую хотите удалить:
>>>''')
    return name_del.title()


def search_del(name, lst):
    file = open("new_text.txt", "w", encoding="utf8")
    for el in lst:
        lst_1 = re.split(", ", el)
        if name != lst_1[0] and len(lst_1) > 1:
            file.write(f"{el}\n")
    os.remove("text.txt")
    file.close()
    os.rename("new_text.txt", "text.txt")
    os.system('cls||clear')
    print("--------------------------------")
    print("Удаление пришло успешно!")
    controller.print_commands()


def get_lst(catalog, identifier):
    lst = []
    lst_0 = catalog.split("\n")
    for el in lst_0:
        lst_1 = re.split(", |;", el)
        for el_1 in lst_1:
            if identifier == el_1:
                lst.append(el)
    return lst
