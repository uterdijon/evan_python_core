'''
Complete Exercise 10.2 (p.120) from the textbook.

'''
def cumsum(l):
    cumlist = []
    previous = 0
    for i in l:
        cumlist.append(i)
        previous += 1
