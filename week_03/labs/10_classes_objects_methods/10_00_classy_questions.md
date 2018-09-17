## Classes and OOP

- What is a class?
    A programmer-defined type.

- How do you define a new class called `MyFirstClass`?
    class MyFirstClass():

- How do you create an object of the class `MyFirstClass`?
    myfirstinstance = MyFirstClass()

- What is instantiation?
    Creating an object that is an instance of a class.

- What are attributes?
    They are objects embedded in a class.

- What does it mean when an object is embedded?
    It is an attribute of another object.

- What is the difference between `copy.copy` and `copy.deepcopy`?
What do they each do?
    The first one does a shallow copy (it does not copy the embedded objects). The second is a deep copy (it copies all the dependencies.)

- What is the difference between a pure function and a modifier?
    A pure function does not change the arguments/attributes. A modifier changes the arguments.

- What is object-oriented programming?
    Doing everything within the framework of an object (for example, using methods inside objects instead of independent functions.) Three tenets: Encapsulation, inheritance, polymorphism.

## Methods (page 161)

- What is a method?
    A function inside and related to an object.
- How is a method different than a function?
    We call it differently: _object.method()
- What is invocation?
    Calling a method on an object.

- What is the `__init__` method and what is it used for?
    This is used for instatiating an object of a given class.

- Give an example `__init__` method for a `Car` class with attributes:
`make`, `model` and `year`.
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


- How do `__init__` methods handle variable arguments?
    ???


- What is the `__str__` method used for?
    This tells the object what to return when a string function is called on it.

- How do you use a `__str__` method?
    For example if we want to display time:

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

- What is operator overloading?
    We can define how operators work on the class we are creating.

- What is an example of operator overloading?

    For example, we can define what the "+" operator does to this class:

        def __add__(self, other):
            seconds = self.time_to_int() + other.time_to_int()
            return int_to_time(seconds)

## TYPE-BASED DISPATCH?

- What is polymorphism?
    Polymorphism is when a function can be called on different types of objects.

- Why is polymorphism beneficial?
    This is beneficial because we do not have to write a different function for each type of object.
