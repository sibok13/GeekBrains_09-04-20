# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.


class Complex:
    def __init__(self, d, m):
        self.d = d
        self.m = m

    def __str__(self):
        tmp = '+' if self.m >= 0 else ''
        return f'{self.d}{tmp}{self.m}j'

    __repr__ = __str__


class Calc:

    def summ(self, c1, c2):
        d = c1.d + c2.d
        m = c1.m + c2.m
        print(Complex(d, m))

    def mul(self, c1, c2):
        d = c1.d * c2.d - c1.m * c2.m
        m = c1.m * c2.d + c1.d * c2.m
        print(Complex(d, m))


calc = Calc()
calc.summ(Complex(2, 4), Complex(1, 2))
calc.mul(Complex(2, 4), Complex(1, 2))
