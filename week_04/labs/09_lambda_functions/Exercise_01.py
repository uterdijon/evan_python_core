'''
Re-write the following listcomp as a lambda expression.

'''

names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']

#print([x.startswith('D') for x in names])

x = list(map((lambda i: i.startswith("D")), names))

print(x)





#check = lambda i, d: i.startswith(d)

#print(check("dog", "d"))

#print(i.startswith(d))


#x = first_let("dog", "e")

#map(first_let "d"), names)
#x = list(map(first_let, names))

#print(x)
