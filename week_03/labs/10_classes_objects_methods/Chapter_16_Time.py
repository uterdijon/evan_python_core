class Time:
    pass
    '''Represents time of day.

    attributes: hour, minute, second'''

class Hour():
    pass

class Minute():
    pass

class Second():
    pass

mytime = Time()
mytime.hour = Hour()
mytime.minute = Minute()
mytime.second = Second()
mytime.hour = 11
mytime.minute = 59
mytime.second = 30

yourtime = Time()
yourtime.hour = Hour()
yourtime.minute = Minute()
yourtime.second = Second()
yourtime.hour = 11
yourtime.minute = 59
yourtime.second = 29

def print_time(time):
    print(time.hour, ":", time.minute, ":", time.second)
    #print('% : % : %' %time.hour %time.minute %time.second)

print_time(mytime)

def is_after(time1, time2):
    minutes1 = (time1.hour * 60) + time1.minute
    seconds1 = (minutes1 * 60) + time1.second
    minutes2 = (time2.hour * 60) + time2.minute
    seconds2 = (minutes2 * 60) + time2.second
    return seconds1 > seconds2

print(is_after(mytime, yourtime))

def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1

    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1

    return sum

start = Time()
start.hour = 9
start.minute = 45
start.second = 0

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

done = add_time(start, duration)
print_time(done)

def increment(time,seconds):
    newtime = Time()
    newtime.second = time.second += seconds

    if newtime.second >= 60:
        newtime.second -= 60
        newtime.minute += 1

    if newtime.minute >= 60:
        newtime.minute -= 60
        newtime.hour += 1

    return newtime
