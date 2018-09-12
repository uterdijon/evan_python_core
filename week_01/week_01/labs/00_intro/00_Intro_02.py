'''
Write the necessary code to print the following to the console:

	PPPP   Y     Y  TTTTTTTTT  H    H      O     N       N
	P   P   Y   Y       T      H    H     O O    N N     N
	P   P    Y Y        T      H    H    O   O   N  N    N
	PPPP      Y         T      HHHHHH    O   O   N   N   N
	P         Y         T      H    H    O   O   N    N  N
	P         Y         T      H    H     O O    N     N N
	P         Y         T      H    H      O     N       N

'''

def print_python():
    x = " "
    p = "P"
    y = "Y"
    t = "T"
    h = "H"
    o = "O"
    n = "N"
    print(4*x, 4*p, 3*x, y, 5*x, y, 2*x, 9*t, 2*x, h, 4*x, h, 6*x, o, 5*x, n, 7*x, n, sep="")
    print(4*x, p, 3*x, p, 3*x, y, 3*x, y, 7*x, t, 6*x, h, 4*x, h, 5*x, o, x, o, 4*x, n, x, n, 5*x, n, sep="")
    print(4*x, p, 3*x, p, 4*x, y, x, y, 8*x, t, 6*x, h, 4*x, h, 4*x, o, 3*x, o, 3*x, n, 2*x, n, 4*x, n, sep="")
    print(4*x, 4*p, 6*x, y, 9*x, t, 6*x, 6*h, 4*x, o, 3*x, o, 3*x, n, 3*x, n,3*x, n, sep="")
    print(4*x, p, 9*x, y, 9*x, t, 6*x, h, 4*x, h, 4*x, o, 3*x, o, 3*x, n, 4*x, n, 2*x, n, sep="")
    print(4*x, p, 9*x, y, 9*x, t, 6*x, h, 4*x, h, 5*x, o, x, o, 4*x, n, 5*x, n, x, n, sep="")
    print(4*x, p, 9*x, y, 9*x, t, 6*x, h, 4*x, h, 6*x, o, 5*x, n, 7*x, n, sep="")
print_python()


