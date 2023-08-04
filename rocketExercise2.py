import math


class Rocket:

    # rocket simulates a rocket ship for a game,

    # or a physics simulation.

    def __init__(self, x=0, y=0):
        # each rocket has an (x,y)position.
        self.x = x
        self.y = y

    def move_rocket(self, x_increment=0, y_increment=1):
        # move the rocket according to the parameters given.
        # default behaviour is to move the rocket up one unit.
        self.x += x_increment
        self.y += y_increment

    def get_distance(self, other_rocket):
        # import math
        # calculates the distance from this rocket to another,
        # and returns that value

        distance = math.sqrt((self.x - other_rocket.x) ** 2 + (self.y - other_rocket.y) ** 2)
        print("The rockets are %f units apart." % distance)

    # performing a safety check
    def safety_check(self, other_rocket):
        dt = math.sqrt((self.x - other_rocket.x) ** 2 + (self.y - other_rocket.y) ** 2)

        if dt == 0:
            print("The rockets have crushed into each other ")
        elif 0 < dt < 10:
            print("The rockets are too close to each other ")
        else:
            print("The rockets are a safe distance apart ")


# moving rocket object and printing position
my_rocket = Rocket(2, 7)
my_rocket.move_rocket(100, 57)
print("My_rocket moves to :", my_rocket.x, my_rocket.y)

# creating a fleet of 4 rockets
rockets = [Rocket() for x in range(4)]

# move each rocket a different amount
rockets[0].move_rocket()
rockets[1].move_rocket(20, 1)
rockets[2].move_rocket(-6, 10)
rockets[3].move_rocket(7, 7)

# show where each rocket is
for index, rocket in enumerate(rockets):
    print("Rocket %d is at (%d,%d). " % (index, rocket.x, rocket.y))

# show the distance between several of the rockets in the fleet.
for i, j in zip(range(0, 3), range(1, 4)):
    print(rockets[i].get_distance(rockets[j]))
