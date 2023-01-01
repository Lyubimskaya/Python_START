# import json
# from os import path


# def get_data() -> list:
#     """
#     Выгружает данные из файла и возвращает список словарей
#     """
#     if path.isdir("db.json"):
#         with open("db.json", 'r', encoding="utf-8") as file:
#             data_file = json.load(file)
#         return data_file["items"]
#     else:
#         return []


# def add_data(data: dict):
#     """
#     Принимает словарь с записью и добавляет в файл..
#     :param data:
#     """
#     if path.isdir("db.json"):
#         with open("db.json", 'r', encoding="utf-8") as file:
#             data_file = json.load(file)
#     else:
#         data_file = []

#     id = len(data_file) + 1
#     data["id"] = id
#     data_file.append(data)

#     with open("db.json", "w", encoding="utf-8") as file:
#         json.dump(data_file, file, indent=2, ensure_ascii=False)

from logger import log
import json


@log
def get_data() -> list:
    """Выгружает данные из файла"""
    with open("db.json", 'r', encoding="utf-8") as f:
        data_file = json.load(f)
    return data_file["items"]


@log
def get_data_id(id: int) -> dict:
    """Возвращает только одну запись по id"""
    with open("db.json", "r", encoding="utf-8") as f:
        data_file = json.load(f)
        for item in data_file['items']:
            if item['id'] == id:
                return item


@log
def get_data_last_name(last_name: str) -> list:
    """Возвращает только одну запись по фамилии"""
    res = []
    with open("db.json", "r", encoding="utf-8") as f:
        data_file = json.load(f)
        for item in data_file['items']:
            if item['last_name'].lower() == last_name.lower():
                res.append(item)
    return res


@log
def add_data(data: dict):
    id = data.get("id")
    """Принимает словарь с записью и добавляет в файл.
    Если в принимаемом словаре имеется поле id, тогда сначала удаляет эту запись из словаря.
    :param data:"""
    with open("db.json", 'r', encoding="utf-8") as f:
        data_file = json.load(f)

    if id:
        for i, items in enumerate(data_file["items"]):
            if id == items["id"]:
                data_file["items"][i] = data
                break

    else:
        id = data_file["last_id"]["id"] + 1
        data_file["last_id"]["id"] = id
        data["id"] = id
        data_file["items"].append(data)

    with open("db.json", "w", encoding="utf-8") as f:
        json.dump(data_file, f, indent=2, ensure_ascii=False)