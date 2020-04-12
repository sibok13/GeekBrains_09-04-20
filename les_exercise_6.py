while True:
    result_first_day = input("Укажите результат первого дня в км:\n")
    result_total = input("Укажите, какой результат вы хотите получить в км:\n")
    if result_first_day.replace(".", "", 1).isdigit() and result_total.replace(".", "", 1).isdigit():
        result_first_day = float(result_first_day)
        result_total = float(result_total)
        break
    else:
        print("Вы ввели не корректные данные, вводите только числа")

day = 1
while result_first_day < result_total:
    day += 1
    result_first_day = result_first_day * 1.1

print(day)
