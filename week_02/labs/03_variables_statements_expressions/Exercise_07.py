'''
In the U.S., if there is:
    - One person who is born every 6 seconds
    - One person who dies every 12 seconds
    - One person who immigrates every 40 seconds

Write the necessary code to display the total population
for the next 3 years (without a leap year).
Let's say the current population is 380,123,456.

'''
**************************
current_pop = 380123456
born_sec = 1.0/6
die_sec = 1.0/12
immigrate_sec = 1.0/40
year = 60 * 60 * 24 * 365
born_year = born_sec * year
die_year = die_sec * year
immigrate_year = immigrate_sec * year
pop_change = born_year - die_year + immigrate_year
pop_year_1 = int(current_pop + pop_change)
pop_year_2 = int(pop_year_1 + pop_change)
pop_year_3 = int(pop_year_2 + pop_change)
print(pop_change)
print(born_sec)
print("The population after one year will be: ",pop_year_1,".",sep="")
print("The population after two years will be: ",pop_year_2,".",sep="")
print("The population after three years will be: ",pop_year_3,".",sep="")
**************************
