'''
Create a Generator that loops over the given sequence and prints out
only the items that are divisible by 1111.

'''

# note: range() also works with a generator object internally
nums = range(1, 1000000)

# creating the generator expression
div_gen = (print(n) for n in nums if (n % 1111 == 0))
# checking on its output - NOTE: the strange seeming syntax,
# resulting from the fact that the print() statement is already part
# of the generator expression!
for n in div_gen:
    n
