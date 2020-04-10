sec = input("Введите время в секундах\n")
hour = int(sec) // 3600
minutes = (int(sec) % 3600) // 60
seconds = int(sec) % 3600 % 60

print("{0:02}:{1:02}:{2:02}" .format(hour, minutes, seconds))
