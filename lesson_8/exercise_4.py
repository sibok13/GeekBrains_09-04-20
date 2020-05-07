# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который
# будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

class Storage:

    storage = {
        'printer': [],
        'copier': [],
        'scanner': []
    }

    def add(self, type_eq, data):
        self.storage[type_eq].append(data)

    def get_total(self):
        result = {}
        for eq_type, eq_list in self.storage.items():
            result[eq_type] = len(eq_list)
        return result


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

Printer2 = Printer()
Printer2.add_item(model='HP', coast=8000, print_speed=800)

Copier1 = Copier()
Copier1.add_item(model='Canon', coast=10000, type_install='table')

Scanner1 = Scanner()
Scanner1.add_item(model='Sony', coast=5000, resolution=1200)

my_storage = Storage
my_storage().add(Printer1.type, Printer1.__dict__)
my_storage().add(Printer2.type, Printer2.__dict__)
my_storage().add(Copier1.type, Copier1.__dict__)
my_storage().add(Scanner1.type, Scanner1.__dict__)

print(my_storage().get_total())
