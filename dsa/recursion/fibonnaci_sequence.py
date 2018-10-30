"""
Fibonnaci Sequence

Implement a Fibonnaci Sequence in three different ways:

- Recursively
- Dynamically (Using Memoization to store results)
- Iteratively

Function Output
Your function will accept a number n and return the nth number of the fibonacci sequence

Remember that a fibonacci sequence: 0,1,1,2,3,5,8,13,21,... starts off with a base case checking to see if n = 0 or 1, then it returns 1.

Else it returns fib(n-1)+fib(n+2).

Hopefully this interview question served as a good excercise in exploring recursion, dynamic programming, and iterative solutions for a single problem! Its good to work through all three because in an interview a common question may just begin with requesting a recursive solution and then checking to se if you can implement the other forms!
"""


def fib_rec(n):
    """Recursively. Solve the problem using simple recursion."""
    pass


# Instantiate Cache information
n = 10
cache = [None] * (n + 1)


def fib_dyn(n):
    """Dynamically. Implement the function using dynamic programming by using a cache to store results (memoization)."""
    pass


def fib_iter(n):
    """Iteratively. Implement the solution with simple iteration."""
    pass