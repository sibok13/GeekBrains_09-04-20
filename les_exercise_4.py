while True:
    data = input("Введите целое положительное число:\n")
    if data.isdigit():
        data = int(data)

        my_list = []
        while data > 0:
            digit = data - (data // 10) * 10
            my_list.append(digit)
            data = (data - digit) // 10

        i = 9
        while i > 0:
            if i in my_list:
                print(i)
                break
            else:
                i -= 1
        break
    else:
        print("Вы ввели не корректное число! Вводите только цифры!")
