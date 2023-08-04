"""# rocket with no class
# x and y value for the rocket
x = 0
y = 0

# creating a set of x and y values for 5 rockets
x_y = ((4,1),(5,3),(3,6),(2,3),(1,1))
rocket1 = x_y[0]
rocket2 = x_y[1]
rocket3 = x_y[2]
rocket4 = x_y[3]
rocket5 = x_y[4]

# creating a list of the five rockets
my_rocket = [rocket1, rocket2, rocket3, rocket4, rocket5]
print(my_rocket[4])
print(x_y[2][1])

print(my_rocket[3])


"""
class Rocket:
    def __init__(self):
        self.x = 2
        self.y = 1

    def moveUp(self):
        self.y += 2

musa = Rocket()
print(musa)
print(musa.y)
musa.moveUp()
musa.moveUp()
musa.moveUp()
print(musa.y)

my_Rocket = []
for h in range(8):
    my_Rocket.append(Rocket())

for g in my_Rocket:
    print(g)
