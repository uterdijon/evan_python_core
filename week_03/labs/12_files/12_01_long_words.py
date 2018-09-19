'''
Write a program that reads in the file words.txt and prints only the
words with more than 20 characters (not counting whitespace).

Source: http://greenteapress.com/thinkpython2/html/thinkpython2010.html

'''

with open("/Users/evan/CodingNomads/test/new_venv/python_core/week_03/labs/12_files/words.txt", "r") as words:
    word_list = words.readlines()

stripped_words = []
for word in word_list:
    word = word.strip("\r\n")
    stripped_words.append(word)

final_list = []
for word in stripped_words:
    if len(word) > 20:
        final_list.append(word)

print(final_list)
