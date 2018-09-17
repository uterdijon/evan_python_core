'''
Using a dictionary, write a function called has_duplicates that takes
a list and returns True if there is any element that appears more than
once.

Solution: http://thinkpython2.com/code/has_duplicates.py.

Source: Chapter "Dictionaries" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2011.html

'''
def has_duplicates(my_list):
    my_dict = {}
    for i in my_list:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    for i in my_dict:
        if my_dict[i] > 1:
            print("True")
            return True

has_duplicates([1,2,3,4,4])
