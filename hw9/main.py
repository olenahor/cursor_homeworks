# TASK 1
# Створити логер який дозволяє працювати з файлами як звичайний open,
# але разом з тим в файл logs.txt записує:
# коли був відкритий файл, назва файла, коли закритий файл
# для інформації про час можемо використати datetime.now()
# приклад відпрацювання
# with my_custom_manager('file.txt', 'r') as f:
#     f.read()
# В файл буде записано
# 2022-07-11 22:17:59.782551 file.txt OPEN
# 2022-07-11 22:18:00.782551 file.txt CLOSE

# TASK 2
# Написати ф-цію яка переводить файл logs.txt в logs.csv
# Приклад такого файлу
# 2022-07-11 22:17:59.782551, file.txt, OPEN
# 2022-07-11 22:18:00.782551, file.txt, CLOSE

import datetime
import pandas as pd


class ContextManager():
    txt_file = 'logs.txt'
    csv_file = 'logs.csv'

    def __init__(self, filename, mode="a+"):
        self.file = open(filename, mode)
        self.filename = filename

    def __enter__(self):
        with open(ContextManager.txt_file, "a") as f:
            opening_record = str(datetime.datetime.now()) + ' ' + self.filename + ' OPEN\n'
            f.write(opening_record)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(ContextManager.txt_file, "a") as f:
            closing_record = str(datetime.datetime.now()) + ' ' + self.filename + ' CLOSE\n'
            f.write(closing_record)
        self.file.close()

    @staticmethod
    def txt_to_csv(input_file, output_file):
        read_file = pd.read_csv(input_file)
        read_file.to_csv(output_file, index=None)


with ContextManager('file.txt') as file:
    print(file.read())

ContextManager.txt_to_csv('logs.txt', 'logs.csv')








