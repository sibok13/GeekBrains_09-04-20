while True:
    sec = input("Введите время в секундах\n")
    if sec.isdigit():
        sec = int(sec)
        hour = sec // 3600
        minutes = (sec % 3600) // 60
        seconds = sec % 3600 % 60
        print("{0:02}:{1:02}:{2:02}".format(hour, minutes, seconds))
        break
    else:
        print("Вы ввели не корректное число, вводите только цифры.")
