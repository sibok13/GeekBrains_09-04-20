# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом
# премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать
# данные, проверить значения атрибутов, вызвать методы экземпляров)

class Worker:
    name = 'n/a'
    surname = 'n/a'
    position = 'n/a'
    _income = {"wage": 0, "bonus": 0}


class Position(Worker):

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])


a = Position()
a.name = 'Петя'
a.surname = 'Иванов'
a.position = 'Менеджер'
a._income = {"wage": 5000, "bonus": 10000}
a.get_full_name()
print(a.position)
a.get_total_income()