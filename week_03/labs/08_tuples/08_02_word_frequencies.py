'''
Write a function called most_frequent that takes a string and prints
the letters in decreasing order of frequency. Find text samples from
several different languages and see how letter frequency varies between
languages. Compare your results with the tables at:
http://en.wikipedia.org/wiki/Letter_frequencies.
Solution: http://thinkpython2.com/code/most_frequent.py.

Source: Chapter on "Tuples" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2013.html

'''

import collections

def most_frequent(source, lang):
    table = {}
    for c in source:
        if c not in table:
            table[c] = 1
        else:
            table[c] += 1
    my_list = list(table.items())
    sorted_list = sorted(my_list, key=lambda tup:(-tup[1], tup[0]))
    print("The frequency of letters in the", lang, "text is: ")
    for i in sorted_list:
        letter, freq = i
        print(letter)


        

'''Table1 = collections.namedtuple('Letter','Frequency')

    sorted_table = sorted([Table1(v,k) for (k,v) in table.items()], reverse=True)
    #OrderedDict(sorted(table.items(), key=lambda x: x[1]))

    
    print(sorted_table)
'''
        
        

def count_german():
    de_text = input("Enter a text in German: ")
    most_frequent(de_text, "German")


def count_french():
    fr_text = input("Enter a text in French: ")
    most_frequent(fr_text, "French")

def count_spanish():
    es_text = input("Enter a text in Spanish: ")
    most_frequent(es_text, "Spanish")

count_german()

count_french()

count_spanish()

#most_frequent("abcdeade")
