'''
Using the tweepy package, build a script that classifies a twitter handle
into different groups according to the number of their followers.

The classes can be whatever you like (e.g. I used ASCII art birds ;)

CHALLENGE: Also fetch the number of their friends and display the ratio
between followers and friends in an interesting way.

'''

import os
import tweepy
from pprint import pprint

# fetch the secrets from our virtual environment variables
CONSUMER_KEY = os.environ['TWITTER_API_KEY']
CONSUMER_SECRET = os.environ['TWITTER_API_SECRET_KEY']
ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
ACCESS_SECRET = os.environ['TWITTER_ACCESS_SECRET']

# authenticate to the service we're accessing
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
# create the connection
api = tweepy.API(auth)


# define a handle to inspect for quicker reference
handle = 'rondaz_g'  # for example purposes; prop any handle you want!
user = api.get_user(handle)
user_data = user._json
num_friends = user.friends_count






'''

class User:
    def __init__(self, handle, friends_count, followers_count):
        self.handle = handle
        self.friends_count = friends_count
        self.followers_count = followers_count
'''




###############################
def add_to_dict(handle):
    #Summary: This function creates a dictionary with each key being a twitter user's handle and each value being a dictionary with each Twitter user attribute as a key and the Twitter attribute value itself as a value.

    #Args:
        #handle (STRING): A Twitter user's handle
    #Returns:
        #dict:   key: Twitter user's handle
                #value:  dictionary: key: Twitter user's data category
                                    #value: Twitter user's data

    user = api.get_user(handle)
    user_data = user._json
    user_dict[handle] = user_data
    return user_dict
##############################

user_dict = {}
add_to_dict('rondaz_g')
add_to_dict('CABI_Invasives')
add_to_dict('CABI_Invasives')
add_to_dict('Roia_ICT')
add_to_dict('phat_controller')
add_to_dict('KutomaW')
add_to_dict('HumaniData')
add_to_dict('Salma_Abbasi')
add_to_dict('joshuacstephens')
add_to_dict('boronatix')
add_to_dict('hustlecrewlive')
add_to_dict('medievalpoc')
add_to_dict('OscarTheGrouch')
add_to_dict('blkgirlculture')
add_to_dict('keciabert')


followers_dict = {}
friends_dict = {}

##############################
def get_attribute(source_dict, target_dict, attribute):
    #This retrieves a particular Twitter attribute from a dictionary of users and their attributes and adds the information to a target dictionary.
    for handle in source_dict:
            target_dict[handle] = source_dict[handle][attribute]
##############################
def print_attribute(source_dict, title):
    #This prints out a title and then on each line one user's handle and the user's value for the attribute.
    print(f"{title}:")
    for handle in source_dict:
        print(f"{handle}: {source_dict[handle]}")
    print("\n")
##############################
def classify_by_attribute(source_dict, title):
    #This function takes a dict of (handle : attribute value) and sorts the items into four quartiles based on the difference between the handle with the highest number of followers and that with the lowest number. It then prints out the four quartiles as a list of tuples.
    quartile1_list = []
    quartile2_list = []
    quartile3_list = []
    quartile4_list = []
    my_max = max(source_dict.items(), key=lambda k: k[1])
    my_min = min(source_dict.items(), key=lambda k: k[1])
    quartile = (my_max[1] - my_min[1]) / 4
    quartile1 = (my_min[1], (my_min[1] + quartile))
    quartile2 = ((my_min[1] + quartile), (my_min[1] + (quartile * 2)))
    quartile3 = ((my_min[1] + (quartile * 2)), (my_min[1] + (quartile * 3)))
    quartile4 = ((my_min[1] + (quartile * 3)), (my_min[1] + (quartile * 4)))
    print(quartile1)
    print(quartile2)
    print(quartile3)
    print(quartile4)
    for handle in source_dict:
        if source_dict[handle] < quartile1[1]:
            quartile1_list.append((handle, source_dict[handle]))
        elif source_dict[handle] > quartile2[0] and source_dict[handle] < quartile2[1]:
            quartile2_list.append((handle, source_dict[handle]))
        elif source_dict[handle] > quartile3[0] and source_dict[handle] < quartile3[1]:
            quartile3_list.append((handle, source_dict[handle]))
        elif source_dict[handle] > quartile4[0] and source_dict[handle] < quartile4[1]:
            quartile4_list.append((handle, source_dict[handle]))
    print(title)
    print(f"Quartile 1: {quartile1_list}")
    print(f"Quartile 2: {quartile2_list}")
    print(f"Quartile 3: {quartile3_list}")
    print(f"Quartile 4: {quartile4_list}")
    print("\n")

    q1 = 'Quartile 1'
    q2 = 'Quartile 2'
    q3 = 'Quartile 3'
    q4 = 'Quartile 4'
    und = '____________________'

    print(f'{q1:<30}{q2:<30}{q3:<30}{q4:<30}')
    print(f'{und:<30}{und:<30}{und:<30}{und:<30}')
    for t in range(len(user_dict)):
        try:
            c1a = quartile1_list[t][0]
        except IndexError:
            c1a = ' '
        try:
            c1b = quartile1_list[t][1]
        except IndexError:
            c1b = ' '
        try:
            c2a = quartile2_list[t][0]
        except IndexError:
            c2a = ' '
        try:
            c2b = quartile2_list[t][1]
        except IndexError:
            c2b = ' '
        try:
            c3a = quartile3_list[t][0]
        except IndexError:
            c3a = ' '
        try:
            c3b = quartile3_list[t][1]
        except IndexError:
            c3b = ' '
        try:
            c4a = quartile4_list[t][0]
        except IndexError:
            c4a = ' '
        try:
            c4b = quartile4_list[t][1]
        except IndexError:
            c4b = ' '

        print(f'{c1a:<15}{c1b:<15}{c2a:<15}{c2b:<15}{c3a:<15}{c3b:<15}{c4a:<15}{c4b:<15}')


    ##############################



get_attribute(user_dict, followers_dict, 'followers_count')
get_attribute(user_dict, friends_dict, 'friends_count')

print_attribute(followers_dict, "Number of Followers")
print_attribute(friends_dict, "Number of Friends")

classify_by_attribute(followers_dict, "Number of Followers:")
classify_by_attribute(friends_dict, "Number of Friends:")
