"""
List Comprehension practice

https://www.reddit.com/r/learnpython/comments/4d2yl7/i_need_list_comprehension_exercises_to_drill/

Tip: Practice mechanically translating a list comprehension into the equivalent for loop and back again.
"""

# Find all of the numbers from 1-1000 that are divisible by 7
seven = [num for num in range(1,1001) if num % 7 == 0]
print(seven)

# Find all of the numbers from 1-1000 that have a 3 in them

# Count the number of spaces in a string
string = 'sample string of text'
spaces = [char for char in string if char == ' ']
total = len(spaces)

# Remove all of the vowels in a string
vowels = 'aeiou'
string = 'a string with vowels'
no_vowels = [char for char in string if char not in vowels]

# Find all of the words in a string that are less than 4 letters
short = [word ]

# Challenge:

# Use a dictionary comprehension to count the length of each word in a sentence.

# Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)

# For all the numbers 1-1000, use a nested list/dictionary comprehension to find the highest single digit any of the numbers is divisible by


"""
From: http://www.learnpython.org/en/List_Comprehensions
"""
# create a list of integers which specify the length of each word in a certain sentence, but only if the word is not the word "the".
lengths = [len(word) for word in sentence.split() if word != 'the']
print(lengths)

# long way
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
      if word != "the":
          word_lengths.append(len(word))
print(words)
print(word_lengths)


# create a new list called "newlist" out of the list "numbers", which contains only the positive numbers from the list, as integers.
newlist = [int(num) for num in numbers if num > -1]
print(newlist)
