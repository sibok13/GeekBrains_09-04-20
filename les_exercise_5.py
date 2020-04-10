revenue = int(input("Укажите прибыль\n"))
costs = int(input("Укажите затраты\n"))

if revenue - costs > 0:
    profit = revenue - costs
    efficiency = profit / revenue
    print("У вас прибыль в размере:", profit)
    print("Ваша рентабильность: {: 0.2F}" .format(efficiency))
    staff = input("Сколько сотрудников работает в вашей компании?\n")
    print("Прибыль вашей компании в расчете на одного сотрудника: {: 0.2F}" .format(profit / int(staff)))
elif revenue - costs == 0:
    print("Вы сработали в ноль!")
else:
    print("У вас убытки в размере:", revenue - costs)
