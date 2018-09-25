# x = input("this is: ")
# print(x)

# for number in range(2, 100):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(number)


# # laura's solution
# # https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops # noqa 503
# # https://python-notes.curiousefficiency.org/en/latest/python_concepts/break_else.html
# # the first URL actually has exactly the prime number example there!
import pdb

pdb.set_trace()
for check_prime in range(1, 100):
    for x in range(2, check_prime):
        if check_prime % x == 0:
            break
    else:
        print(check_prime)
