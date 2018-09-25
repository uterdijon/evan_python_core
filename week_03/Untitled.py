'''
_list = [1,2,3,4,5]
temp = 0
for i in range(len(_list)):
    temp += _list[i] * (10 ** (i+1))

for i in range(len(_list)):
    _list[i] = temp / (10 ** ((len(_list) - i)))
    temp -= _list[i] * (10 ** ((len(_list) - i)))

print(_list)

##########################

_list = [1,2,3,4,5]

for i in range(len(_list)/2):
    temp = _list[i]
    _list[i] = _list[(len(_list) - 1) - i]
    _list[(len(_list) - 1) - i] = temp

print(_list)
'''
print 3
