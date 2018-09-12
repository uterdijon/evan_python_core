'''
If a runner runs 12 kilometers in 30 minutes and 30 seconds.
What is his/her average speed in miles per hour. (Tip: 1 mile = 1.6 km)

'''
*******************
distance_km = 12
hours = 0
minutes = 30
seconds = 30
time_in_seconds = (hours * 60 * 60) + (minutes * 60) + seconds
speed_km_sec = distance_km / time_in_seconds
speed_km_hr = speed_km_sec * (60 * 60)
speed_mi_sec = speed_km_sec * 0.621
speed_mi_hr = speed_mi_sec * (60 * 60)
print("The runner's average speed is: ",speed_mi_hr," mph",".",sep="")

*******************
