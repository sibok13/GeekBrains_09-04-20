# тип переменной сделал float, так как результат может быть не целым числом (например, 1.5 км)

result_km = float(input("Укажите результат первого дня в км:\n"))
expectation = float(input("Укажите, какой результат вы хотите получить в км:\n"))

day = 1
while result_km < expectation:
    day += 1
    result_km = result_km * 1.1

print(day)