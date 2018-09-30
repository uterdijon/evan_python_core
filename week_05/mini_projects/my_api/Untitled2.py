import time
import datetime

def get_unixtime(year, month, day):
      #takes a year, month, and day as arguments and returns the unix time
      dateTime = datetime.date(year, month, day)
      unixtime = str(time.mktime(dateTime.timetuple()))
      return unixtime

def get_month_avg(month):
    get



def get_10_dates(month):
    #Takes a month number (1-12) as argument and returns a list of 10 unix times for the 15th of that month over the last 10 years.
    now = datetime.datetime.now()
    year = (now.year - 11)
    date_list = []
    data_list = []
    for i in range(11):
        unixtime = get_unixtime(year, month, 15)
        date_list.append(unixtime)
        year += 1
    return(date_list)


print(get_month_avg(1))
