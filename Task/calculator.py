class calc:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        sum = self.a + self.b
        print(sum)
    
    def sub(self):
        sub = self.a - self.b
        print(sub)

    def mul(self):
        mul = self.a * self.b
        print(mul)

    def div(self):
        div = self.a / self.b
        print(div)

a = int(input('Enter first no.: '))
b = int(input('Enter second no.: '))

obj = calc(a , b)

choice = int(input('Enter your choice (1 for add, 2 for sub, 3 for mul, 4 for div) => '))

if choice == 1:
    obj.add()
elif choice == 2:
    obj.sub()
elif choice == 3:
    obj.mul()
elif choice == 4:
    obj.div()