from logger import log
import model
from tabulate import tabulate


@log
def greatings():
    '''Вывод приветствия'''

    print('Cправочник учеников школы.')


@log
def close_prog():
    '''Выход из справочника'''

    print('Вы вышли из справочника.')


@log
def print_error(msg=""):
    '''Вывод ошибки'''

    print(f'Ошибка. {msg}')


@log
def menu():
    '''Вывод меню'''

    return input('Что Вы хотите сделать: \n'
                 '   1. Посмотреть справочник \n'
                 '   2. Добавить строку в справочник \n'
                 '   3. Редактировать строку справочника \n'
                 '   4. Удалить строку справочника \n'
                 '   5. Завершить работу \n'
                 'Для выбора введите номер пункта: ')


@log
def print_record_data(record):
    '''Вывод данных строки справочника'''

    print('\n')
    for key in model.my_dict.keys():
        print(f'  {model.my_dict.get(key)}: {record[key]}')
    print('\n')


@log
def print_records(data):
    '''Печать справочника'''

    print(tabulate(data, headers=model.my_dict, tablefmt="grid"))