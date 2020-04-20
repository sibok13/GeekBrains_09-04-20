# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает
# сумму наибольших двух аргументов.

def my_func(a, b, c):
    """
    Принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
    :param a: int
    :param b: int
    :param c: int
    :return: int
    """
    my_list = [a, b, c]
    max_num_1 = max(my_list)
    my_list.pop(my_list.index(max_num_1))
    max_num_2 = max(my_list)
    result = max_num_1 + max_num_2
    print(result)
    return


my_func(20, 5, 30)
