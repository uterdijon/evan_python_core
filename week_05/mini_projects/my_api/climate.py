from pprint import pprint
import requests
from locations import cities



for place in locations.cities:
    url = self.create_url(place)


class MyApp():


    def create_url(self, place):
        city, country = place
        query = f'address={city}+{country}'
        url = f'http://www.datasciencetoolkit.org/maps/api/geocode/json?{query}'
        return url

    def add_coord(self, place):
        url = self.create_url(place)
        r = requests.get(url)
        city_coord = data = r.json()

'''
r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=\
                    London,uk&appid=b2175c44ff368c401ed884482283a418",
                    json=True)
"location": {"lat": 37.42382, "lng": -122.08999},

city_locations = {
    'Madrid': (40.416775, -3.703790)
    'Barcelona': (41.385063, 2.173404)
    'Valencia': (39.470242, -0.376800)






}



#DARK_SKY_KEY = os.environ['DARK_SKY_KEY']

DARK_SKY_KEY = 0fcd0937d43a26c91f822901a94d1cc8
https://api.darksky.net/forecast/[latitude],[longitude],[time]



r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=\
                    London,uk&appid=b2175c44ff368c401ed884482283a418",
                    json=True)


data = r.json()

# pprint(r.headers)
pprint(data)
# print(type(data))

print(data['visibility'])







#import json
#import sys

#import os
#import tweepy
#from pprint import pprint

# fetch the secrets from our virtual environment variables
#CONSUMER_KEY = os.environ['TWITTER_API_KEY']
#CONSUMER_SECRET = os.environ['TWITTER_API_SECRET_KEY']
#ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
#ACCESS_SECRET = os.environ['TWITTER_ACCESS_SECRET']

# authenticate to the service we're accessing
#auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
# create the connection
#api = tweepy.API(auth)


# define a handle to inspect for quicker reference
#handle = 'rondaz_g'  # for example purposes; prop any handle you want!
#user = api.get_user(handle)
#user_data = user._json
#num_friends = user.friends_count

#user = api.get_user(handle)
#    user_data = user._json
#    user_dict[handle] = user_data
#    return user_dict




class MyApp:

    def dispatch(self, environ):
        query = environ['QUERY_STRING']
        method = environ['REQUEST_METHOD']
        path = environ['PATH_INFO']
        address = environ['REMOTE_ADDR']
        fileinfo = self.filereader()
        words = self.word_list(query)

        if method == 'GET' and path == '/inventory':
            inven = json.dumps(fileinfo)
            return inven

        elif method == 'POST' and path == '/inventory':
            self.create_product(words, fileinfo)
            self.display_status(fileinfo, words)

        elif method == 'PATCH' and path == '/inventory':
            self.augment_quantity(words, fileinfo)
            self.display_status(fileinfo, words)

        elif method == 'DELETE' and path == '/inventory':
            self.delete_product(words, fileinfo)
            return f'There are currently 0 {words[0][1]} in the inventory.'



    def create_product(self, words, fileinfo):
        if words[0][1] in fileinfo:
                return 'This item is already in the inventory.'
        else:
                fileinfo[words[0][1]] = 0
        self.filewriter(fileinfo)

    def delete_product(self, words, fileinfo):
        if words[0][1] in fileinfo:
            del fileinfo[words[0][1]]
        else:
            return 'This item is not in the inventory.'
        self.filewriter(fileinfo)

    def augment_quantity(self, words, fileinfo):
        if words[0][1] in fileinfo:
            fileinfo[words[0][1]] += int(words[1][1])
        else:
            return f'There is no such item {words[0][1]} in the inventory. Please add it.'
        self.filewriter(fileinfo)

    def display_status(self, fileinfo, words):
        return f'There are currently {fileinfo[words[0][1]]} {words[0][1]} in the inventory.'

    def word_list(self, query):
        words = []
        for pair in query.split('&'):
            one_word = pair.split('=')
            words.append(one_word)
            return words

    def filewriter(self, fileinfo):
        json.dump(fileinfo, open('/Users/evan/CodingNomads/python_core/week_05/mini_projects/server_from_scratch/inventory_api.txt', 'w'))
        return 'Your inventory has been updated'

    def filereader(self):
        _dict = {}
        with open('/Users/evan/CodingNomads/python_core/week_05/mini_projects/server_from_scratch/inventory_api.txt', 'r') as f:
            _dict = json.loads(f.read())
        return _dict
