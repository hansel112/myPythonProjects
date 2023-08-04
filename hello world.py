'''print("Hello world!")
name = 'Paul'
age = 29
salary = 6000.5345
print('My name is %s. I am %d years old. I earn %0.2f shillings.'% (name, age, salary))
dghjjlkjkl;iyiuy
dbjh
bjjh'''

class Car:
    def __init__(self, make, model, year, N_D, owner):
        self.m = make
        self.mod = model
        self.y = year
        self.n = N_D
        self.o = owner

    def describe_car(self):
        print(f"The {self.m} car of {self.mod} produced in {self.y} with {self.n} doors is for {self.o}")

class Track(Car):
    def __init__(self,make, model, year, N_D, owner, N_T,weight):
        super().__init__(make, model, year, N_D, owner)
        self.t = N_T
        self.w = weight

    def more_description(self):
        print(f"It has {self.t} tyres and carries a weight of {self.w} tonnes")
        

my_car = Car('Subaru', 'c300', 2022, 4, 'Sempo')
car1 = Car('Bez', 'Bd43', 2021, 2, 'Paul')
car2 = Track('Tata', 'r23', 2020,2, 'Sam', 10, 10)
print(my_car.m)
print(my_car.mod)
print(my_car.y)
print(my_car.n)
print(my_car.o)
print()
my_car.describe_car()
car1.describe_car()
print()
car2.describe_car()
car2.more_description()