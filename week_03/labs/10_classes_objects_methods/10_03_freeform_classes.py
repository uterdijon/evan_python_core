'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the + operator in one of the classes
    so that it adds two attributes of that class.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...

'''

class Animal():
    move = True
    reproduce = 'sexually'

    def __init__(self, name, limbs=4, locomotion='walking', hair='does not', eggs='does not'):
        self.name = name
        self.limbs = limbs
        self.locomotion = locomotion
        self.hair = hair
        self.eggs = eggs

    def __str__(self):
        return 'The {0} is an animal, which means it moves and reproduces {1}. It has {2} limbs and moves by {3}. It {4} have hair and {5} lay eggs.'.format(self.name, self.reproduce, self.limbs, self.locomotion, self.hair, self.eggs)

    def __add__(self, other):
        result = '{0} and {1}'.format(self, other)
        return result



dog = Animal('dog', 4, 'walking', 'does', 'does not')
dove = Animal('dove', 2, 'flying', 'does not', 'does')

print(dog)
print(dove)
print(dog.name + dog.hair)
