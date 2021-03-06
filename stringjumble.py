"""
stringjumble.py
Author: Ryan Kynor
Credit: 
http://stackoverflow.com/questions/1009160/reverse-the-ordering-of-words-in-a-string

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
text = input("Please enter a string of text (the bigger the better): ")


print ('You entered "{0}". Now jumble it:'.format(text))

#writes all letters in reverse order
print (text [::-1])

#writes the words in reverse order
print (" ".join(text.split()[::-1]))

#writes letters within a word in reverse order - text2 is a temporary variable
text2 = " ".join(text.split()[::-1])
print (text2[::-1])


