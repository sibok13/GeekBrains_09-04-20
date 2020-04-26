# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('test.txt', 'x', encoding='UTF-8') as my_file:
    print('Введите текст для записи в файл:')
    while True:
        my_text = input()
        if my_text == '':
            break
        else:
            print(my_text, file=my_file)
