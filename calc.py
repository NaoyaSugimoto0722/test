# 四則演算をするモジュール

class Calc:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

if __name__ == '__main__':
    calc = Calc()
    print(calc.add(1, 2))
    print(calc.sub(1, 2))
    print(calc.mul(1, 2))
    print(calc.div(1, 2))
