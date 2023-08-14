import main
import busines_logik_2
import controller
import os
import re




def add_book():
    os.system('cls||clear')
    book_name = busines_logik_2.chek_book()
    book_author = input("Введите автора книги: ")
    book_year_of_publishing = busines_logik_2.check_date()
    book_genre = input("Введите жанр книги: ")
    info = f"{book_name}, {book_author.title()}, {book_year_of_publishing}, {book_genre.title()};\n"
    file = open("text.txt", "a", encoding="utf8")
    file.write(info)
    file.close()
    os.system('cls||clear')
    print("-----------------------------------")
    print("Новая книга добавлена в каталог.")
    controller.print_commands()


def read_catalog():
    os.system('cls||clear')
    catalog = busines_logik_2.get_catalog()
    print(catalog)
    controller.print_commands()

def search_book():
    os.system('cls||clear')
    identifier = controller.get_identifier()
    catalog = busines_logik_2.get_catalog()
    lst = busines_logik_2.get_lst(catalog, identifier)
    if len(lst) == 0:
        os.system('cls||clear')
        print("-------------------------------")
        print("По вашему запросу ничего не найдено!")
        controller.print_commands()
    os.system('cls||clear')
    print("------------------------------")
    print("По вашему запросу наидено:")
    for el in lst:
        print(el)
    controller.print_commands()

def delite_book():
    os.system('cls||clear')
    name_del = busines_logik_2.get_name_del()
    catalog = busines_logik_2.get_catalog()
    lst = catalog.split("\n")
    count = 0
    for el in lst:
        lst_1 = re.split(", |;", el)
        if name_del == lst_1[0] and len(lst_1) > 1:
            count += 1
    if count != 0:
         busines_logik_2.search_del(name_del, lst)
    os.system('cls||clear')
    print("-------------------------------")
    print("По вашему запросу ничего не найдено!")
    controller.print_commands()


def sort_book():
    ...

def treatment_command(command):
    if command.upper() == "R":
        read_catalog()
    elif command.upper() == "A":
        add_book()
    elif command.upper() == "S":
        search_book()
    elif command.upper() == "D":
        delite_book()

    else:
        exit()

