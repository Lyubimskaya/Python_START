from logger import log
import json
from os import path

database = []
my_dict = {'id': 'ID',
           'first_name': 'Имя',
           'last_name': 'Фамилия',
           'birth_day': 'Дата рождения',
           'phone': 'Номер телефона',
           'class': 'Класс'
           }


@log
def get_data():
    """
    Загружает данные из файла и возвращает список словарей.
    """
    global database
    if path.isfile("handbook.json"):
        with open("handbook.json", 'r', encoding="utf-8") as f:
            database = json.load(f)
    else:
        database = []


@log
def save_data():
    """
    Сохраняет данные в файл
    """

    with open("handbook.json", "w", encoding="utf-8") as f:
        json.dump(database, f, indent=2, ensure_ascii=False)


@log
def get_record(num: int) -> dict:
    """
    Загружает данные из файла и возвращает словарь с индексом.
    :param num:
    """
    num = num - 1
    record = []
    if num >= 0 and num <= len(database) - 1:
        record = database[num]
    return record


@log
def add_record(data: dict):
    """
    Принимает словарь с записью и добавляет в файл.
    :param data:
    """
    global database
    id = len(database) + 1
    data["id"] = id
    database.append(data)
    save_data()


@log
def delete_record(num: int):
    """
    Удаляет строку справочника по индексу и записывает в файл.
    :param num: int
    """
    global database
    num = num - 1
    if num >= 0 and num <= len(database) - 1:
        database.remove(database[num])
        save_data()


@log
def edit_record(num: int, data: dict):
    """
    Принимает словарь с записью и заменяет словарь с индексом.
    :param num: int, data: dict
    """
    global database
    num = num - 1
    if num >= 0 and num <= len(database) - 1:
        database[num].update(data)
        save_data()