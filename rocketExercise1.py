class Rocket:
    def __init__(self, x=0, y=0):
        # each rocket has an (x,y) position
        self.x = x
        self.y = y

    def move_up(self):
        # default behaviour is to move the rocket up one unit
        self.x += 1
        self.y += 1

    # describing self
    def describes(self):
        # printing the object
        print(f"My_rocket is at position ({self.x},{self.y})")
        # printing the object's y-value
        print(f"My_rocket is at altitude {self.y}")


# creating rocket object
my_rocket = Rocket(2, 15)
my_rocket.describes()

# moving Rocket_0 up
my_rocket.move_up()
print("My_rocket moves up to altitude: ", my_rocket.y)

# creating a fleet of rockets
my_rockets = [Rocket() for x in range(4)]

# showing that each rocket is a separate object
for rocket in my_rockets:
    print(rocket)
