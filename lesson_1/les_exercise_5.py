while True:
    revenue = input("Укажите прибыль\n")
    costs = input("Укажите затраты\n")
    if revenue.replace(".", "", 1).isdigit() and costs.replace(".", "", 1).isdigit():
        revenue = float(revenue)
        costs = float(costs)
        break
    else:
        print("Вы ввели не корректные данные, вводите только числа")

if revenue - costs > 0:
    profit = revenue - costs
    efficiency = profit / revenue
    print("У вас прибыль в размере: {: 0.2F}" .format(profit))
    print("Ваша рентабильность: {: 0.2F}" .format(efficiency))
    staff = input("Сколько сотрудников работает в вашей компании?\n")
    print("Прибыль вашей компании в расчете на одного сотрудника: {: 0.2F}" .format(profit / int(staff)))
elif revenue - costs == 0:
    print("Вы сработали в ноль!")
else:
    print("У вас убытки в размере:", revenue - costs)
