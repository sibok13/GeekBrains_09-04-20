messege_1 = "Добрый день! Как вас зовут? \n"
year = 2020
messege_3 = "До скорой встречи!"

name = input(messege_1)
age = input("Привет, " + name + ", сколько тебе лет?\n")
print(name, ", тебе", age, "лет и это отличный возраст!")
print("Если тебе сейчас", age, "лет, то год твоего рождения", year - int(age), ".")
print(messege_3)
