'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''

def my_enumerate(iterable, start=0):
    new_list = []
    for i in range(start,len(iterable)):
        new_tuple = (i, iterable[1])
        new_list.append(new_tuple)
    return new_list

courses = ['Intro', 'Intermediate', 'Advanced', 'Epic Hero']

my_list = my_enumerate(courses, 1)
print(my_list)
