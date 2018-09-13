'''
Complete Exercise 10.7 (p.121) - the birthday paradox - from the textbook.

'''


def has_duplicates(l):
    new_list = []
    for i in l:
        if i in new_list:
            print("True")
            return True
        else:
            new_list.append(i)

my_list = [1,2,3,4,5]
has_duplicates(my_list)
