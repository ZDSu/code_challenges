# Edit the function provided by calling partial() and replacing the first three variables in func(). Then print with the new partial function using only one input variable so that the output equals 60.

#Following is the exercise, function provided:
from functools import partial
def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x
#Enter your code here to create and print with your partial function


# my solution
new = partial(func, 10, 4, 3)
print(new(2))


# their solution
p = partial(func,5,6,7)
print(p(8))
