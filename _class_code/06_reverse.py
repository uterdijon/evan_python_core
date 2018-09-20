# nope
_list = [1, 2, 3, 4, 5, ]
for i in range(len(_list)):
    _list[i] = _list[len(_list) - 1 - i]

print(_list)

# same nope
_list = [1, 2, 3, 4, 5, ]
store = 0
for i in range(len(_list) // 2):
    store = _list[i]
    _list[i] = _list[len(_list) - 1 - i]

print(_list)

# yep works!
_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
store = 0
for i in range(len(_list) // 2):
    store = _list[i]
    _list[i] = _list[len(_list) - 1 - i]
    _list[len(_list) - 1 - i] = store

print(_list)
