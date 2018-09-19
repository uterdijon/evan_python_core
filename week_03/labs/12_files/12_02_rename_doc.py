'''
Write a function called sed that takes as arguments a pattern string,
a replacement string, and two filenames; it should read the first file
and write the contents into the second file (creating it if necessary).
If the pattern string appears anywhere in the file, it should be
replaced with the replacement string.

If an error occurs while opening, reading, writing or closing files,
your program should catch the exception, print an error message,
and exit.
Solution: http://thinkpython2.com/code/sed.py.


Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html

'''
def sed(pat_string, rep_string, file1, file2):
    try:
        new_file = ("file2" + ".txt")
    except FileNotFoundError:
        msg = "Can't find file {0}.".format(f_name)
        print(msg)
        break

    try:
        with open("file1","r") as file1:
            new_string = file1.read()
    except FileNotFoundError:
        msg = "Can't find file {0}.".format(f_name)
        print(msg)
        break

    try:
    with open(new_file, 'w') as new_file:
        file2.write(new_string)
        for str in new_file:
            if str == pat_string:
                new_file.replace(str, rep_string)

    except FileNotFoundError:
        msg = "Can't find file {0}.".format(f_name)
        print(msg)
        break
        
    return new_file
