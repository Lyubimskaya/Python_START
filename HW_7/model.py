import json
from os import path


def get_data() -> list:
    """
    Выгружает данные из файла и возвращает список словарей
    """
    if path.isdir("db.json"):
        with open("db.json", 'r', encoding="utf-8") as file:
            data_file = json.load(file)
        return data_file["items"]
    else:
        return []


def add_data(data: dict):
    """
    Принимает словарь с записью и добавляет в файл..
    :param data:
    """
    if path.isdir("db.json"):
        with open("db.json", 'r', encoding="utf-8") as file:
            data_file = json.load(file)
    else:
        data_file = []

    id = len(data_file) + 1
    data["id"] = id
    data_file.append(data)

    with open("db.json", "w", encoding="utf-8") as file:
        json.dump(data_file, file, indent=2, ensure_ascii=False)