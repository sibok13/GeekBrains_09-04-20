while True:
    data = input("Введите число\n")
    if data.isdigit():
        result = int(data) + int(data + data) + int(data + data + data)
        print("Ответ:", result)
        break
    else:
        print("Вы ввели не корректное число, вводите только цифры.")
