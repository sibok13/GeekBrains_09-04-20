# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
# draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = 'Stationery'

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):
        print('Обводка ручкой.')

class Pencil(Stationery):
    def draw(self):
        print('Тонировка карадашем.')

class Handle(Stationery):
    def draw(self):
        print('Закрашивание маркером.')


a = Pen()
a.draw()
b = Pencil()
b.draw()
c = Handle()
c.draw()
