import busines_logik_1
import os


def print_commands():
    print("------------------------------")
    print("Выберите комманду:")
    str = "asdrASDRqQ"
    command = input(f'''
Если хотите посмотреть каталог, нажмите "R";
Если хотите добавить книгу, нажмите "A";
Если хотите найти книгу, нажмите "S";
Если хотите удалить книгу, нажмите "D";
Есди хотите выйти нажмите "Q".
>>>>''')
    while command not in str:
        os.system('cls||clear')
        print("-------------------------------")
        print("Некорректный ввод")
        command = input(f'''
Если хотите посмотреть каталог, нажмите "R";
Если хотите добавить книгу, нажмите "A";
Если хотите найти книгу, нажмите "S";
Если хотите удалить книгу, нажмите "D";
Есди хотите выйти нажмите "Q".
>>>>''')
    busines_logik_1.treatment_command(command)


def get_identifier():
    os.system('cls||clear')
    print("------------------------------")
    identifier = input('''
Если хотите найти книгу, введите ее название;
Введите автора, если хотите найти его произведения;
Введите жанр, если хотите найти книги по жанру;
>>>''')
    return identifier.title()
