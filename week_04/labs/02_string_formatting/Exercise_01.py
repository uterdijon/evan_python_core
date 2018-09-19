'''
Using f-strings, print out the name, last name, and favorite
office supply item of each person in the given dictionary,
formatted like so:

LASTNAME, Name           Office supply item
LONGERLASTNAME, Name     Office supply item

'''

office = [
    {"full_name": "Michael Scott", "item": "world's best boss mug"},
    {"full_name": "Dwight Schrute", "item": "pepper spray"},
    {"full_name": "Jim Halpert", "item": "phone"},
    {"full_name": "Pam Beesly", "item": "post-its"},
    {"full_name": "Ryan Howard", "item": "business cards"},
    {"full_name": "Stanley Hudson", "item": "crossword-puzzle"},
    {"full_name": "Kevin Malone", "item": "m&ms"},
    {"full_name": "Meredith Palmer", "item": "flask"},
    {"full_name": "Angela Martin", "item": "cat food"},
    {"full_name": "Oscar Martinez", "item": "calculator"},
    {"full_name": "Phyllis Lapin", "item": "cut flowers"},
    {"full_name": "Kelly Kapoor", "item": "People magazine"},
    {"full_name": "Toby Flenderson", "item": "files"},
    {"full_name": "Creed Bratton", "item": "mung beans"},
    {"full_name": "Darryl Philbin", "item": "forklift"},
]

#ASTNAME, Name           Office supply item
names = []
items = []
first_names = []
last_names = []
upper_last_names = []
for i in office:
    names.append(i['full_name'])
    items.append(i["item"])

for i in names:
    first, last = i.split()
    first_names.append(first)
    last_names.append(last)

for i in last_names:
    i = i.upper()
    upper_last_names.append(i)

print(names)
print(items)
print(first_names)
print(upper_last_names)


for i in range(len(first_names)):
    print(f"{upper_last_names[i] + ', '+ first_names[i]:<20} {items[i]}")
