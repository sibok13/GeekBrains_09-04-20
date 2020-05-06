# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который
# будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

class Storage:

    __storage_capacity = 100

    def __init__(self, total_amount):
        self.total_amount = total_amount

class Equipment:

    def __init__(self, tool_type, model, coast, amount):
        self.tool_type = tool_type
        self.model = model
        self.coast = coast
        self.amount = amount

class Printer(Equipment):

    def __init__(self, tool_type, model, coast, amount, print_speed):
        super().__init__(tool_type, model, coast, amount)
        self.print_speed = print_speed

class Copier(Equipment):

    def __init__(self, tool_type, model, coast, amount, type_install):
        super().__init__(tool_type, model, coast, amount)
        self.type_install = type_install

class Scanner(Equipment):

    def __init__(self, tool_type, model, coast, amount, resolution):
        super().__init__(tool_type, model, coast, amount)
        self.resolution = resolution
