'''
--------------------------------------------------------
                PROGRAMMED SONG LYRICS
--------------------------------------------------------

Programmatically create your own song lyrics with multiple verses,
interlaced with a repeating chorus.

Train using string methods and loops on an open-end mini-project!

- use one block of text as verse input (hint: linebreaks can be helpful!)
- use a for loop for creating the full lyrics

'''
##############
def print_lyrics():
    chorus

lyrics = "I like to program, yes I do;I program red, I program blue.Programming is so much fun;I'll program til the work is done.Python is so fun to learn;Sing along, now it's your turn"
chorus = "Program, program, program, we love to write that program"

verse = lyrics.split(".")
for v in verse:
    stanza = v.split(";")
    print(stanza[0],stanza[1],chorus,sep = "\n")
##############
