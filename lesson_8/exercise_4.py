# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
# данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class NotNum(ValueError):

    def __init__(self, txt):
        self.txt = txt

def isint(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

class Storage:
    storage = {
        'printer': [],
        'copier': [],
        'scanner': []
    }

    online_store = {
        'printer': [],
        'copier': [],
        'scanner': []
    }

    def add(self, data, amount):
        try:
            if isint(amount):
                i = 0
                while i < amount:
                    self.storage[data.type].append(data.__dict__)
                    i += 1
            else:
                raise NotNum('Ошибка ввода! Количество товара может быть только целым числом.')

        except NotNum as err:
            print(err)

    def get_total(self, locate):
        if locate == 'storage':
            result = {}
            for eq_type, eq_list in self.storage.items():
                result[eq_type] = len(eq_list)
            print(f'Товары на складе: {result}')
        elif locate == 'online_store':
            result = {}
            for eq_type, eq_list in self.online_store.items():
                result[eq_type] = len(eq_list)
            print(f'Товары в магазине: {result}')
        else:
            print(f'Склада {locate} не существует')

    def moving(self, type_eq, amount):
        print(f'\nПеремещение товара "{type_eq}" {amount} шт., остатки по складам: ')
        i = 0
        while i < amount:
            if len(my_storage().storage[type_eq]) > 0:
                self.online_store[type_eq].append(my_storage().storage[type_eq].pop())
                i += 1
            else:
                print(f'ВНИМАНИЕ! Оборудование "{type_eq}" закончилось. Не хватило {amount - i} шт.')
                break
        my_storage().get_total("storage")
        my_storage().get_total("online_store")

class Equipment:
    model: str
    coast: int

    def add_item(self, **kwargs):
        self.__dict__.update(kwargs)


class Printer(Equipment):
    type = 'printer'
    print_speed: int


class Copier(Equipment):
    type = 'copier'
    type_install: str


class Scanner(Equipment):
    type = 'scanner'
    resolution: int


Printer1 = Printer()
Printer1.add_item(model='Canon', coast=5000, print_speed=1000)

Copier1 = Copier()
Copier1.add_item(model='Canon', coast=10000, type_install='table')

Scanner1 = Scanner()
Scanner1.add_item(model='Sony', coast=5000, resolution=1200)

my_storage = Storage
my_storage().add(Printer1, 5)
my_storage().add(Copier1, 2)
my_storage().add(Scanner1, 3)
my_storage().get_total('storage')
my_storage().get_total('online_store')
my_storage().moving('printer', 2)
