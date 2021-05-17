class Person:
    def __init__(self, name, age, address):
        self.name=name
        self.age=age
        self.address=address

    def greeting(self):
        print(f'안녕하세요. 제 이름은 {self.name}이고, 나이는 {self.age}세, 사는곳은 {self.address}입니다.')

    @staticmethod
    def main():
        john = Person('John', 28, 'Seoul')
        john.greeting()
        jane = Person('Jane', 30, 'Daegu')
        jane.greeting()

if __name__=="__main__":
    Person.main()
