import view
from logger import log
import model
import request


@log
def start():
    view.greatings()
    model.get_data()
    while True:
        match view.menu():
            case '1':  # Посмотреть справочник
                view.print_records(model.database)
            case '2':  # Добавить строку в справочник
                newrecord = request.input_record_data()
                model.add_record(newrecord)
            case '3':  # Редактировать строку справочника
                recordnum = request.input_record_number()
                record = model.get_record(recordnum)
                if record != []:
                    view.print_record_data(record)
                    newrecord = request.input_record_data()
                    model.edit_record(recordnum, newrecord)
                else:
                    view.print_error('Строка не найдена !')
            case '4':  # Удалить строку справочника
                recordnum = request.input_record_number()
                model.delete_record(recordnum)
            case '5':  # Закончить работу
                break
            case _:
                view.print_error()
    view.close_prog()