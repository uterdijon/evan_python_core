'''
Build a simple aggregator function.

'''

my_list = ["goblin", "vampire", "werewolf", "troll"]




def my_aggregator(_list):
        for i in range(len(_list)):
            print("{} : {}".format(i+1, _list[i]))

my_aggregator(my_list)
