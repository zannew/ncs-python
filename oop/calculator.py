class Calculator:
    def __init__(self, first, second):
        self.first=first
        self.second=second

    def sum(self):
        return self.first + self.second
    def sub(self):
        return self.first - self.second
    def mul(self):
        return self.first * self.second
    def div(self):
        return self.first / self.second

    @staticmethod
    def execute():
        calc = Calculator(int(input("첫번째 숫자 : ")), int(input("두번째 숫자 : ")))
        print(f'첫번째 숫자 : {calc.first}')
        print(f'두번째 숫자 : {calc.second}')
        print(f'{calc.first} + {calc.second} = {calc.sum()}')
        print(f'{calc.first} - {calc.second} = {calc.sub()}')
        print(f'{calc.first} * {calc.second} = {calc.mul()}')
        print(f'{calc.first} / {calc.second} = {calc.div()}')


if __name__=='__main__':
    Calculator.execute()
