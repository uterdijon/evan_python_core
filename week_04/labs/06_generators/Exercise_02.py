'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''
nums = range(1, 1000000)

div_by_1111 = (num for num in nums if num % 1111 == 0)

new_list = [num // 1111 for num in div_by_1111]

print(new_list)
