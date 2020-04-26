# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('ex_5', 'x', encoding='UTF-8') as my_file:
    print('10 20 30 40 50 60 70 80 90 100', file=my_file)

with open('ex_5', 'r', encoding='UTF-8') as my_file:
    data_sum = 0
    for line in my_file:
        temp = line.split()
        for i in temp:
            try:
                result = int(i)
                data_sum += result
            except ValueError:
                data_sum += 0

    print(data_sum)
