_list = [1,2,3,4,5]
temp = 0
for i in range(3):
    temp += _list[i] * (10 ** (i+1))

_list2 = []

for i in range(1,3):
    _list2[0] = temp / 10 ** (len(_list) - 1)

print(_list2) 



'''
for i in range(len(_list),-1):
    _list[i-(i-2)] = temp/(list[len(list)-1])
'''

