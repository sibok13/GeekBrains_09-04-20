# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

my_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open('ex_4', 'r', encoding='UTF-8') as my_file:
    for line in my_file:
        for (key, val) in my_dict.items():
            if key in line:
                new_line = line.replace(key, val)
        with open('ex_4_new', 'a', encoding='UTF-8') as my_file_new:
            print(new_line, end='', file=my_file_new)
