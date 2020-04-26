# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

firms_analytics = []
firms_dic = {}
with open('ex_7', 'r', encoding='UTF-8') as my_file:
    for line in my_file:
        temp = line.split()
        try:
            profit = int(temp[2]) - int(temp[3])
        except TypeError:
            pass
        firms_dic.update({temp[0]: profit})

firms_analytics.append(firms_dic)

firm_with_profit = 0
sum_profit = 0
for key, val in firms_dic.items():
    if val >= 0:
        firm_with_profit += 1
        sum_profit += val

average_profit = sum_profit / firm_with_profit
firms_analytics.append({'average_profit': average_profit})
print(firms_analytics)

with open('ex_7.json', 'w', encoding='UTF-8') as j_file:
    json.dump(firms_analytics, j_file)
