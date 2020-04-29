# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

from random import choice as choice

class Car:
    speed = '160'
    color = 'white'
    name = 'Vesta SW'
    is_police = False

    def go(self):
        print('Начало движения')

    def stop(self):
        print('Остановка, окончание движения')

    def turn(self):
        direction = choice(('на лево', 'на право'))
        print(f'Поворот {direction}')

    def show_speed(self, speed):
        if self == TownCar and speed > 60:
            print('Превышение скорости!')
        elif self == WorkCar and speed > 40:
            print('Превышение скорости!')
        else:
            print(f'Ваша скорость {speed}')


TownCar = Car()
TownCar.name = 'BMW'
TownCar.speed = 180
print(TownCar.name)
print(TownCar.is_police)
TownCar.show_speed(100)
print('----------------')

SportCar = Car()
SportCar.name = 'Ferrari'
SportCar.speed = 360
SportCar.color = 'Red'
print(SportCar.name)
print(SportCar.is_police)
print('----------------')

WorkCar = Car()
WorkCar.name = 'Jeep'
print(WorkCar.name)
print(WorkCar.is_police)
WorkCar.show_speed(50)
print('----------------')

PoliceCar = Car()
PoliceCar.name = 'Ford'
PoliceCar.is_police = True
print(PoliceCar.name)
print(PoliceCar.is_police)
PoliceCar.show_speed(160)
print('----------------')
