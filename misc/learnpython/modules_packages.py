# In this exercise, you will need to print an alphabetically sorted list of all functions in the re module, which contain the word find.

import re

# Your code goes here
import re

# Your code goes here
res = []
for function in dir(re):
    if 'find' in function:
        res.append(function)
print(sorted(res))
