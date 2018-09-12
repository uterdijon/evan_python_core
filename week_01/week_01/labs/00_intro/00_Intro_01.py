'''
1 - Write and execute a script that prints "hello world" to the console.

#******************
print("hello world")
#******************

2 - Using the interpreter, print "hello world!" to the console.

3 - Explore the interpreter.
	- Execute lines with syntax error and see what the response is.
        * What happens if you leave out a quotation or parentheses?
	
	
        * How helpful are the error messages?
	- Use the help() function to explore what you can do with the interpreter.
        For example execute help('print').
        press q to exit.
	- Use the interpretor to perform simple math.
	- Calculate how many seconds are in a year.
	
#******************
def calc_sec():
    #a function for calculating the number of seconds in a year
    min = 60
    hour = 60*min
    day = 24*hour
    year = 365*day
    print("There are", year, "seconds in a year.")
    
calc_sec()
#******************
