'''
Build on 10_03_freeform_classes from the section on Classes, Objects and
Methods.
Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in 10_03_freeform_classes.

If you cannot think of a way to build on your previous exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''
class Business():
    def __init__(self, name, location="None", year=0, size=0):
        self.location = location
        self.year = year
        self.size = size
        self.name = name

    def __str__(self):
        return "{} is a business located in {}.".format(self.name, self.location)

    def get_year(self):
        print("{} has been in business since {}.".format(self.name, self.year))

    def get_size(self):
        print("{} has {} employees.".format(self.name, self.size))

    def get_location(self):
        print("{} is located in {}.".format(self.name, self.location))

class Caterer(Business):
    can_eat = False
    makes_food = True

    def __init__(self, name, cuisine, price, location, year, size):
        Business.__init__(self, name, location, year, size)
        self.cuisine = cuisine
        self.price = price

    def get_cuisine(self):
        print("{} serves {} food.".format(self.name, self.cuisine))

    def get_price(self):
        print("The food at {} costs between {} and {}.".format(self.name, self.price[0], self.price[1]))


class Restaurant(Business):
    can_eat = True
    makes_food = True

    def __init__(self, name, cuisine, price, location, year, size):
        Business.__init__(self, name, location, year, size)
        self.cuisine = cuisine
        self.price = price

    def get_cuisine(self):
        print("{} serves {} food.".format(self.name, self.cuisine))

    def get_price(self):
        print("The food at {} costs between {} and {} Euros.".format(self.name, self.price[0], self.price[1]))

class Franchise(Restaurant):
    in_chain = True

    def __init__(self, name, cuisine, price, location, year, size, chain):
        Restaurant.__init__(self, name, cuisine, price, location, year, size)
        Franchise.chain = chain

    def get_chain(self):
        print("{} is a franchise of the chain {}.".format(self.name, self.chain))

class Independent(Restaurant):
    in_chain = False

    def __init__(self, name, cuisine, price, location, year, size):
        Restaurant.__init__(self, name, cuisine, price, location, year, size)

    def get_chain(self):
        print("{} is not part of a chain.")

mcdonalds_barcelona = Franchise("McDonalds 1101", "fast food", (5, 10), "Barcelona", 2001, 30, "McDonalds")

wok_amb_gracia = Independent("Wok amb Gracia", "Asia", (5,10), "Barcelona", 2016, 10)

fancy_rest = Independent("La Tarantella", "Italian", (15,30), "Madrid", 1983, 12)

wok_amb_gracia.get_price()
fancy_rest.get_location()
print(fancy_rest)
print 7
