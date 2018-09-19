# Files

Read through chapter ["Case Study: Word Play"](http://greenteapress.com/thinkpython2/html/thinkpython2010.html) as well as chapter ["Files"](http://greenteapress.com/thinkpython2/html/thinkpython2015.html) from
Allen B. Downey's Think Python 2e book.

- How do you open a file in read mode and print the first line?

with open("name.txt", "r") as f:
  print(f.readline())

- How can you use a for loop to iterate through the words of a file?
  with open("my_file.txt", "r") as f:
    my_list = f.readlines()
    for w in my_list:
      bla bla bla

- What does it mean when a program is persistent?
  The program does not disappear when you exit the interpreter, but rather when you open it again, it continues where you left off.

- How do you open a file in write mode?

    with open("my_file", "w") as f:
      blablabla

- Practice using f-strings as a replacement for the .format() method
  print(f"Hello, my name is {name} and I am {age} years old.")

- What is the difference between a relative path and an absolute path?
    A relative path is just the name of the file and can be used if it is located in the same folder as the script you are running. Otherwise, you must use an absolute path, which includes the entire path from the home directory.

- What are some IOExceptions that you might encounter? How are they generated?
    An IOException is generated when the script is not able to retrieve a file, for example: “file not found” or “disk full”.

- What is a try statement used for?
    This is used when we want to handle exceptions. We tell the interpreter to try something out and then provide except statements to handle the different possible exceptions.

- What is an except statement used for?
    The except statements tell the interpreter what to do in the case of a particular exception.

- Can you have a try without an except? Can you have an except without a try?
    ???

- What is the variable `__name__` used for?
    __name__ gets automatically set to the name of the current module, but if the module is being run directly, it is set to the string "__main__". This allows us to test whether the script is being run directly or being imported by something else by:
        if __name__ == "__main__":
            blablabla
