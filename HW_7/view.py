# from logger import log


# @log
# def greatings():
#     '''Вывод приветствия.'''

#     print('Справочник')
#     pass


# @log
# def menu() -> int:
#     """
#     Вывод меню, запрос данных от пользователя.
#     :return:
#     0 - Выход
#     1 - Загрузить из файла и вывести на экран
#     2 - Добавить новую запись
#     3 - Редактировать запись по id
#     4 - Поиск по фамилии
#     """
#     print('Меню')
#     print(
#         '0 - Выход \n1 - Загрузить из файла и вывести на экран \n2 - Добавить новую запись \n3 - Редактировать запись по id \n4 - Поиск по фамилии \n')
#     return int(input("Введите пункт меню: "))


# @log
# def print_book(data: list):  # список
#     """
#     Вывод в консоль данных содержимого справочника
#     """
#     for my_dict in data:
#         print(f'Имя: {my_dict["first_name"]} | Фамилия: {my_dict["last_name"]}'
#                  '| Телефон: ', *my_dict["phone_number"], f' | Дата рождения: {my_dict["birthday"]}'
#                  f'| Id: {my_dict["id"]}')
#         print("----")
#     if not data:
#         print("<-Нет данных для отображения->")
#         print()


# @log
# def add_record() -> dict:  # введите фамили (ключ имя словарь)
#     """
#     Диалог добавления записи.
#     :return Cловарь с данными записи.:
#     """
#     my_dict = {}
#     tel_list = []

#     my_dict['first_name'] = input('Введите имя : ')
#     my_dict['last_name'] = input('Введите фамилию : ')
#     while True:
#         data = input('Введите номер телефона (для выхода нажмите Enter) : ')
#         if data:
#             tel_list.append(data)
#         else:
#             break
#     my_dict['phone_number'] = tel_list
#     my_dict['birthday'] = input('Дата рождения: ')
#     return my_dict


# @log
# def request_id() -> int:  # ввидите id input
#     """
#     Запрос id от пользователя
#     :return id:
#     """
#     return int(input('Введите id: '))


# @log
# def editor(data: dict) -> dict:  # входит справочник пройти по нему
#     """
#     :param data: Выбранная запись
#     :return отредактированная запись:
#     """
#     new_dict = {}
#     data['first_name'] = input(f"Имя: {data['first_name']}. Введите новое имя: ")

#     data['last_name'] = input(f"Фамилия: {data['last_name']} Введите новую фамилию: ")
#     print("Телефон:", *data['phone_number'])
#     tel_list = []
#     while True:
#         tel = input('Введите номер телефона (для выхода нажмите Enter) : ')
#         if tel:
#             tel_list.append(tel)
#         else:
#             break
#     data['phone_number'] = tel_list
#     data['birthday'] = input(f"Дата рождения: {data['birthday']} Введите новую дату: ")

#     return data


# @log
# def request_last_name() -> str:  # input введите фамилию
#     """
#     Запрос фамилии от пользователя
#     :return фамилия:
#     """
#     return input('Введите Фамилию: ')

from logger import log


@log
def grettings():
    '''Приветствие'''
    print('Я справочник')


@log
def menu() -> str:
    '''Меню справочника'''
    return input('Выберите пункт меню: \n'
                 '1 - показать справочник \n'
                 '2 - добавить запись \n'
                 '3 - выход \n')


@log
def print_book(data: list):
    for el in data:
        print(
            f'Имя: {el["first_name"]} | {el["last_name"]} | {el["phone_number"]} | {el["birthda"]} | {el["workplace"]} | {el["id"]}')
    if not data:
        print('Нет данных для отображения')


@log
def input_data():
    book = {}
    book['id'] = ''
    book["first_name"] = input('Введите имя: ')
    book["last_name"] = input('Введите фамилию: ')
    book["phone_number"] = input('Введите телефон: ')
    book["birthda"] = input('Введите дату рождения: ')
    book["workplace"] = input('Введите место работы: ')
    return book