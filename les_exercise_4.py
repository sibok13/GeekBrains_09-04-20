data = int(input("Введите целое положительное число:\n"))

while data > 0:
    data1 = data - (data // 10) * 10
    print(data1)
    data = (data - data1) // 10
