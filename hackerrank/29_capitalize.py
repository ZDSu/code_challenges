# https://www.hackerrank.com/challenges/capitalize/problem


# Complete the solve function below.
def solve(s):
    s = s.split(' ')
    for i in range(len(s)):
        s[i] = s[i].capitalize()
    return ' '.join(s)

# make sure to specify to split on ' ' because will fail if there are multiple spaces in a row