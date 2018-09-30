from pprint import pprint
import requests
from locations import cities
import json
import time
import datetime


class MyApp():
    pass

class MyPlace():
    def __init__(self, name):
        self.name = name
        self.jan = {}
        self.feb = {}
        self.mar = {}
        self.apr = {}
        self.may = {}
        self.jun = {}
        self.jul = {}
        self.aug = {}
        self.sep = {}
        self.oct = {}
        self.nov = {}
        self.dec = {}

    def create_url(self, place):
        #Takes a tuple of city and country and returns the url to request coordinates from datasciencetookkit.org.
        city, country = place
        query = f'address={city}+{country}'
        url = f'http://www.datasciencetoolkit.org/maps/api/geocode/json?{query}'
        return url

    def add_crds(self, place):
        #Takes a tuple of city and country and returns the lat and lng as a tuple.
        url = self.create_url(place)
        r = requests.get(url)
        city_info = r.json()
        lat = city_info['results'][0]['geometry']['location']['lat']
        lng = city_info['results'][0]['geometry']['location']['lng']
        return (lat, lng)

    def get_weather(self, place, ds_key, time):
        #Takes a place and time as arguments and returns a json object with the weather data for that place and time.
        crds = self.add_crds(place)
        url =f'https://api.darksky.net/forecast/{ds_key}/{crds[0]},{crds[1]},{time}?exclude=currently,hourly,alerts,flags&units=si'
        r = requests.get(url)
        r = r.text
        r = json.loads(r)
        return r

    def get_min_temp(self, place, ds_key, time):
        #Takes a place and time as arguments and returns the value of the minimum temperature for that place and time.
        min_temp = self.get_parameter(place, ds_key, time, "temperatureMin")
        return min_temp

    def get_max_temp(self, place, ds_key, time):
        #Takes a place and time as arguments and returns the value of the maximum temperature for that place and time.
        max_temp = self.get_parameter(place, ds_key, time, "temperatureMax")
        return max_temp

    def get_dew_point(self, place, ds_key, time):
        #Takes a place and time as arguments and returns the value of the dew point for that place and time.
        dew_point = self.get_parameter(place, ds_key, time, "dewPoint")
        return dew_point

    def get_cloud_cover(self, place, ds_key, time):
        #Takes a place and time as arguments and returns the value of the cloud cover for that place and time.
        cloud_cover = self.get_parameter(place, ds_key, time, "cloudCover")
        return cloud_cover

    def get_wind_speed(self, place, ds_key, time):
        #Takes a place and time as arguments and returns the value of the wind speed for that place and time.
        wind_speed = self.get_parameter(place, ds_key, time, "windSpeed")
        return wind_speed

    def get_humidity(self, place, ds_key, time):
        #Takes a place and time as arguments and returns the value of the humidity for that place and time.
        humidity = self.get_parameter(place, ds_key, time, "humidity")
        return humidity

    def get_precipitation(self, place, ds_key, time):
        #Takes a place and time as arguments and returns the value of the precipitation for that place and time.
        precipitation = self.get_parameter(place, ds_key, time, "precipIntensity")
        return precipitation

    def get_parameter(self, place, ds_key, time, parameter):
        #Takes a place, time, and parameter as arguments and returns the value of the parameter for that place and time.
        weather = self.get_weather(place, ds_key, time)
        parameter = weather["daily"]["data"][0][parameter]
        return parameter

    def get_unixtime(self, year, month, day):
        #takes a year, month, and day as arguments and returns the unix time
        dateTime = datetime.date(year, month, day)
        unixtime = str(time.mktime(dateTime.timetuple()))
        return unixtime

    def get_10_dates(self, month):
        #Takes a month number (1-12) as argument and returns a list of 10unix times for the 15th of that month over the last 10 years.
        now = datetime.datetime.now()
        year = (now.year - 11)
        date_list = []
        for i in range(11):
            unixtime = self.get_unixtime(year, month, 15)
            date_list.append(int(float(unixtime)))
            year += 1
        return(date_list)

    def get_month_avg(self, place, ds_key, month, parameter):
        #Takes a place, month, and parameter and returns the average for that parameter on the 15th of that month over the previous 10 years.
        date_list = self.get_10_dates(month)
        value_list = []
        for date in date_list:
            new_value = self.get_parameter(place, ds_key, date, parameter)
            value_list.append(new_value)
        month_avg = sum(value_list) / len(value_list)
        return month_avg




    def get_month_profile(self, place, ds_key):
        min_temp = abself.get_month_avg(place, ds_key, month, "temperatureMin")
        self.jan[min_temp] = min_temp


        for month in range(1,13):
            self.get_month_avg(place, ds_key, month, "temperatureMin")
            {}














obj = MyApp()
ds_key = '0fcd0937d43a26c91f822901a94d1cc8'
unixtime = 1168819200
print(obj.get_precipitation(cities[1], ds_key, unixtime))

print(obj.get_month_avg(cities[1], ds_key, 1, "temperatureMin"))
