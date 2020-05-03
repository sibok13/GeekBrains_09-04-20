# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

from random import choice as choice

class Car:

    is_police = False

    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = False

    def go(self):
        print('Начало движения')

    def stop(self):
        print('Остановка, окончание движения')

    def turn(self):
        direction = choice(('на лево', 'на право'))
        print(f'Поворот {direction}')

    def show_speed(self):
        print(f'Ваша скорость {self.speed}')

class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости! Ваша скорость {self.speed}')
        else:
            print(f'Ваша скорость {self.speed}')

class SportCar(Car):

    color = "Red"

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости! Ваша скорость {self.speed}')
        else:
            print(f'Ваша скорость {self.speed}')


class PoliceCar(Car):
    is_police = True


Car1 = TownCar('BMW', 'Black', 180)
print(Car1.name)
print('Машина полиции:', Car1.is_police)
Car1.go()
Car1.turn()
Car1.show_speed()
Car1.stop()
print('----------------')

Car2 = SportCar('Ferrari', 'Red', 360)
print(Car2.name)
print('Машина полиции:', Car2.is_police)
Car2.go()
Car2.turn()
Car2.show_speed()
Car2.stop()
print('----------------')

Car3 = WorkCar('Jeep', 'White', 50)
print(Car3.name)
print('Машина полиции:', Car3.is_police)
Car3.go()
Car3.turn()
Car3.show_speed()
Car3.stop()
print('----------------')

Car4 = PoliceCar('Ford', 'White', 160)
print(Car4.name)
print('Машина полиции:', Car4.is_police)
Car4.go()
Car4.turn()
Car4.show_speed()
Car4.stop()
print('----------------')
