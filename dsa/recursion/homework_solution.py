def fact(n):
    """
    Returns factorial of n (n!).
    Note use of recursion
    """
    # BASE CASE!
    if n == 0:
        return 1
    
    # Recursion!
    else:
        return n * fact(n-1)


def rec_sum(n):
    """
    Problem 1
    Write a recursive function which takes an integer and computes the cumulative sum of 0 to that integer

    For example, if n=4 , return 4+3+2+1+0, which is 10.

    This problem is very similar to the factorial problem presented during the introduction to recursion. Remember, always think of what the base case will look like. In this case, we have a base case of n =0 (Note, you could have also designed the cut off to be 1).

    In this case, we have: n + (n-1) + (n-2) + .... + 0
    """
    if n == 0:
        return 0

    else:
        return n + rec_sum(n - 1)

    # using helper function
    def helper(n, sum):
        if n == 0:
            return sum
        sum += n
        return helper(n-1, sum)
    return helper(n, 0)


def sum_func(n):
    """Given an integer, create a function which returns the sum of all the individual digits in that integer. For example: if n = 4321, return 4+3+2+1"""
    if len(str(n)) == 1:
        return n
    else:
        return n % 10 + sum_func(n // 10)

    # using helper function
    def helper(n, sum):
        if len(str(n)) == 1:
            sum += n
            return sum
        sum += n % 10
        return helper(n // 10, sum)
    return helper(n, 0)


def word_split(phrase,list_of_words, output = None):
    """
    Note, this is a more advanced problem than the previous two! It aso has a lot of variation possibilities and we're ignoring strict requirements here.

    Create a function called word_split() which takes in a string phrase and a set list_of_words. The function will then determine if it is possible to split the string in a way in which words can be made from the list of words. You can assume the phrase will only contain words found in the dictionary if it is completely splittable.
    """
    pass