def mul_time(time, number):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    new_seconds = seconds * number
    new_minutes, new_time.second = divmod(seconds, 60)
    new_time.hour, new_time.minute = divmod(minutes, 60)
    return new_time
