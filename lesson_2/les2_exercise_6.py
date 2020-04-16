# *Реализовать структуру данных ​ «​ Товары​ »​ . Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента ​— номер товара и словарь
# с параметрами (характеристиками товара: название,  цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

product_list = []
item_num = 1
while True:
    new = input('Нажмите Y, если хотите добавить новый товар, или любую другую клавишу для отмены\n')

    if new == 'y':
        product = {'Название': None, 'Цена': None, 'Количество': None, 'Ед.изм.': None}
        for k, v in product.items():
            print('Укажите ', k, 'товара')
            product[k] = input()
        item = (item_num, product)
        product_list.append(item)
        item_num += 1
    else:
        break
print(product_list)

if not product_list:
    print('Нет товаров для анализа!')
else:
    print('АНАЛИТИКА ТОВАРОВ:')

    data = {}
    counter = 0
    for k, v in product_list[counter][counter + 1].items():
        feature = []
        for i in product_list:
            tmp = i[1]
            feature.append(tmp[k])
        new_data = {k: feature}
        data.update(new_data)

    print(data)
