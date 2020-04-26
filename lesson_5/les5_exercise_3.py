# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('ex_3', 'r', encoding='UTF-8') as my_file:
    n = 0
    workers = []
    for lines in my_file:
        n += 1
        line = lines.split()
        line = [int(el) if el.isdigit() else el for el in line]
        workers.append(line)

print('Сотрудники с зарплатой ниже 20 000 руб.')

for element in workers:
    if element[2] < 20000:
        print('-', element[0])

workers_sum = len(workers)
salary_sum = 0
for element in workers:
    salary_sum += element[2]

average = salary_sum / workers_sum

print('Средний доход сотрудников:', average, 'руб.')
