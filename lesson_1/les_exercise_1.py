messege_1 = "Добрый день! Как вас зовут? \n"
messege_2 = "До скорой встречи!"
year = 2020

name = input(messege_1)
age = input("Привет, " + name + ", сколько тебе лет?\n")

if age.isdigit():
    age = int(age)
    year_birth = year - age
else:
    year_birth = age

print(name, ", тебе", age, "лет и это отличный возраст!")
print("Если тебе сейчас", age, "лет, то год твоего рождения", year_birth, ".")
print(messege_2)
