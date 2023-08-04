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

    def get_distance(self, other_rocket, x1=0, y1=0):
        # import math
        # calculates the distance from this rocket to another,
        # and returns that value.
        other_rocket.x = x1
        other_rocket.y = y1

        distance = math.sqrt((self.x - other_rocket.x) ** 2 + (self.y - other_rocket.y) ** 2)
        return distance


class Shuttle(Rocket):
    # shuttle stimulates a space shuttle which is just a reusable rocket
    def __init__(self, x=0, y=0, max_flights=0):
        super().__init__(x, y)
        self.max_flights = max_flights

    def support_spacewalks(self):
        print("Supports spacewalks. ")

    def dock_ISS(self):
        print("Docking with the ISS. ")

    def radiation_protection(self):
        print("Protects against radiation. ")


shuttle_21 = Shuttle(19, 6, 10)
shuttle_21.radiation_protection()
