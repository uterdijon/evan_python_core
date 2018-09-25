#4.0 * (1 - (1/3) + (1/5) - (1/7) + (1/9) - (1/11))

# build pi with a loop

num = 1
flag = True

for odd in range(3, 1000002, 2):
    if flag:
        num -= (1 / odd)
        flag = False
    else:
        num += (1 / odd)
        flag = True

print(4 * (num))
