# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится
# месяц (зима, весна, лето, осень) . Напишите решения через list и через dict.

month = input('Введите месяц в виде целого числа\n')

seasons_list = [['Зима', '12', '1', '2'], ['Весна', '3', '4', '5'], ['Лето', '6', '7', '8'], ['Осень', '9', '10', '11']]
seasons_dict = {
    '1': 'Зима',
    '2': 'Зима',
    '3': 'Весна',
    '4': 'Весна',
    '5': 'Весна',
    '6': 'Лето',
    '7': 'Лето',
    '8': 'Лето',
    '9': 'Осень',
    '10': 'Осень',
    '11': 'Осень',
    '12': 'Зима'
}

i = 0
for data in seasons_list:
    tmp = data
    if month in data:
        print("Значение списка:", data[0])
        break

if month in seasons_dict.keys():
    print("Значение словаря:", seasons_dict[month])
