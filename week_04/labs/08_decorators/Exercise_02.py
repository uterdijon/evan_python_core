'''
Improve the decorator from the previous exercise by allowing it to take
a tag as an input - making it more general.

'''
def make_paragraph(func):
    def wrapper_func(name, tag):
        return f"<{func(tag)}>{func(name)}</{func(tag)}>"
    return wrapper_func



@make_paragraph
def capitalize(name):
    name = name.upper()
    return(name)

x = capitalize("Evan", "p")
print(x)
