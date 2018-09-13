'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple


Notes:
    If the user enters an odd numbered list, add the last item
    to a tuple with the number 0.


'''
def process_list(numbers):

    sort_num = sorted(numbers)
    new_list = []
    if len(numbers) % 2 != 0:
           numbers.append(0)
    i = numbers[0]
    while numbers.index(i) <= (len(numbers)-1):
        first_value = i
        second_value = numbers[(numbers.index(i) + 1)]
        new_pair = (first_value, second_value)
        new_list.append(new_pair)
        if numbers.index(i) < (len(numbers) - 2):
            i = numbers[numbers.index(i) +2]
        else:
            break
    for i in new_list:
            print(i)       
        

process_list([1,2,3,4,5])
