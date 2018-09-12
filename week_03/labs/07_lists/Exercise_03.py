'''
Complete Exercise 10.1 (p.120) from the textbook.

Sum up all elements from a nested list of integers.



Write a function called nested_sum that takes a list of lists of integers and
 adds up the elements from all of the nested lists. For example:

>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t)
21

 '''

def nested_sum(l):
    sum = 0
    for i in l:
        for e in i:
            sum += e
    print(sum)

t = [[1, 2], [3], [4, 5, 6]]
a = nested_sum(t)
