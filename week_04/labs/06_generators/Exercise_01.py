'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''

# remember: range() also creates a generator object (try printing it!)
nums = range(1, 1000000)

div_by_1111 = (num for num in nums if num % 1111 == 0)

for num in div_by_1111:
    print(num)
