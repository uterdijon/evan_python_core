'''
Write a decorator function that wraps text passed to it in <p> tags.

'''


def make_paragraph(func):
    def wrapper_func(name):
        beg_p = "<p>"
        end_p = "</p>"
        return f"{beg_p}{func(name)}{end_p}"
    return wrapper_func



@make_paragraph
def capitalize(name):
    name = name.upper()
    return(name)

x = capitalize("Evan")
print(x)
