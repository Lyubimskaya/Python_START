from logger import log
import model



@log
def input_record_number():

    return int(input('Введите номер строки справочника: '))


@log
def input_record_data():

    print('Введите данные строки: ')
    record = {}
    for key in model.my_dict.keys():
        if key != 'id':
            record[key] = input(f'  {model.my_dict.get(key)}: ')
    return record