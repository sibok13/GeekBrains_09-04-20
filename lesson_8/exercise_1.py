# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:

    def __init__(self, date_str, day=0, month=0, year=0):
        self.date_str = date_str
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def str_date(cls, date_str):
        day, month, year = map(int, date_str.split('-'))
        result = cls(date_str, day, month, year)
        return result

    @staticmethod
    def valid_date(date_str):
        day, month, year = map(int, date_str.split('-'))
        return day <= 31 and month <= 12 and year <= 2021


date1 = '20-05-2020'
main_date = Date.str_date(date1)
print(f'Дата в текстовом виде: {main_date.date_str}')
print(F'День: {main_date.day}, месяц: {main_date.month}, год: {main_date.year}')
main_date_is_date = Date.valid_date(date1)
print(f'Проверка на корректность ввода даты: {main_date_is_date}')
