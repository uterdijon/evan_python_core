'''
--------------------------------------------------------
                99 BOTTLES OF BEER LYRICS
--------------------------------------------------------

https://www.reddit.com/r/beginnerprojects/comments/19kxre/project_99_bottles_of_beer_on_the_wall_lyrics/

-- GOAL --
Create a program that prints out every line to the song
"99 bottles of beer on the wall." This should be a pretty simple program,
so to make it a bit harder, here are some rules to follow.

-- RULES --
1) If you are going to use a list for all of the numbers,
    do not manually type them all in. Instead, use a built in function.
2) Besides the phrase "take one down," you may not type in any
    numbers/names of numbers directly into your song lyrics.
3) Remember, when you reach 1 bottle left, the word "bottles" becomes singular.
4) Put a blank line between each verse of the song.

'''
<<<<<<< HEAD


numbers = []
for i in range(0,100):
    numbers.append(i)
for n in numbers:
    print(n)

    print(n," bottles of beer on the wall, ",n," bottles of beer. Take one down and pass it around, ",n," bottles of beer on the wall.")



=======
#******************
numbers = []
for i in range(0,100):
    numbers.append(i)
for n in reversed(numbers):
    if n > 1:
        print(n," bottles of beer on the wall, ",n," bottles of beer. Take one down and pass it around, ",n-1," bottles of beer on the wall.\n",sep="")
    elif n == 1:
        print(n," bottle of beer on the wall, ",n," bottle of beer. Take one down and pass it around, no more bottles of beer on the wall.\n",sep="")
    elif n == 0:
        print("No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.")
 #******************
>>>>>>> f1276b90e80fc9cd04b8b1d31a20dead4e710bb0
