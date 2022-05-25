class Calculator:
    def __init__(self, a, b, oper):
        self.a = b
        self.b = b
        self.oper = oper

    def calc(self):
        if self.oper == "+":
            print(self.a + self.b)
        if self.oper == "-":
            print(self.a - self.b)
        if self.oper == "*":
            print(self.a * self.b)
        if self.oper == "/" and self.b != 0:
            print(self.a / self.b)
        else:
            print("Неправельная операция")

calculator = Calculator(5, 5, "*")
calculator.calc()
