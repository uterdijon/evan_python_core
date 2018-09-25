class Animal(object):
    """docstring for Animal"""
    body = True
    def __init__(self):
        self.substance = "carbon"

class Mammal(Animal):
    """
        A clade of endothermic amniotes distinguished from reptiles
        (including birds) by the possession of a neocortex (a region of the
        brain), hair, three middle ear bones, and mammary glands.

        Attributes:
            glands (str): Description
            way_of_moving (st): Description

        Deleted Attributes:
            hair (str): Description
    """
    def __init__(self, animal_type, way_of_moving, color):
        # the next two lines do the same (different syntax):
        # calling the superclasses __init__ method
        Animal.__init__(self)
        # super(Mammal, self).__init__()
        # ------------------------------------------------
        # without the Animal init, self.body is still going to be available,
        # however, self.substance is NOT going to be available
        self.glands = "has glands"  # this is inherent for a Mammal!
        self.animal_type = animal_type
        self.way_of_moving = way_of_moving
        self.color = None

    def move(self, distance):
        """
            Moves the mammal by a certain distance.

            Args:
                distance (int): the distance in meters

            Returns:
                str: a sentence describing the mammal's movement
        """
        return f"{self.animal_type} {self.way_of_moving}s {distance} meters"

    def __str__(self):
        return f"{self.animal_type} | {self.way_of_moving}"

class Whale(Mammal):
    """docstring for Whale"""
    def __init__(self):
        Mammal.__init__(self, "whale", "swim", "blue")


willy = Whale()
print(willy.body)
willy.move(30)

print(willy)
print(willy.__str__())
print(willy.__str__().__str__().__str__().__str__().__str__().__str__().__str__().__str__())
