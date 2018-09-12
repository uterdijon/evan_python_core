'''
Complete Exercise 10.3 (p.121) from the textbook.

'''

def middle(l):
    new_list = []
    for i in l:
        new_list.append(i)
    del new_list[0]
    list_len = len(new_list)
    del new_list[list_len - 1]
    return(new_list)

my_list = [1, 2, 3, 4]
middle(my_list)
