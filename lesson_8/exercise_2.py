# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.


class NullErr(Exception):

    def __init__(self, txt):
        self.txt = txt


user_input1 = input("Введите число делимое: ")
user_input2 = input("Введите число делитель: ")

try:
    if int(user_input2) == 0:
        raise NullErr("Ошибка! Деление на 0 запрещено.")
    else:
        result = float(user_input1) / float(user_input2)
        print(result)
except ValueError:
    print("Вы ввели не число")
except NullErr as err:
    print(err)
