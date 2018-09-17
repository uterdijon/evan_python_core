'''
Create a new dictionary using the three dictionaries below.
Then print out each key-value pair.

'''


dict_1 = {1: 1, 2: 4}
dict_2 = {3: 9, 4: 16}
dict_3 = {5: 25, 6: 36, 7: 49}

dict_4 = {}
dict_4.update(dict_1)
dict_4.update(dict_2)
dict_4.update(dict_3)

for i in dict_4:
    print i, dict_4[i]

