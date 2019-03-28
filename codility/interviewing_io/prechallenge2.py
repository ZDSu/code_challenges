"""
Mary has N candies. The i-th candy is of a type represented by an interger T[i].

Mary's parents told her to share the candies with her brother. She must give him exactly half the candies. Fortunately, the number of candies N is even. 

After giving away half the candies, Mary will eat the remaining ones. She loves variety, so she wants to have candies of various types. Can you find the maximum number of different types of candy that Mary can eat? 

Write a function:
    [Java] class Solution { puiblic int solution(int[] T); }
    [Python] def solution(T)
that, given an array T of N integers, representing all the types of candies, returns the maximum possible number of different types of candy that Mary can eat after she has given N/2 candies to her brother. 

For example, given:
    T = [3, 4, 7, 7, 6, 6]
the function should return 3. One optimal strategy for Mary is to give away one candy of type 4, one of type 7 and one of type 6. The remaining candies would be [3, 7, 6]: three candies of different types.

Given:
    T = [80, 80, 1000000000, 80, 80, 80, 80, 80, 80, 123456789]
the function should also return 3. Here, Mary starts with ten candies. She can give away five candies of type 80 and the remaining candies would be [1000000000, 123456789, 80, 80, 80]. There are only three different types in total, i.e. 80, 1000000000 and 123456789.

Write an efficient algorithm for the following assumptions:
- N is an integer within the range [2 .. 100,000];
- N is even;
- each element of array T is an integer with the range  
"""


def candy(candies):
    diff = set(candies)
    if len(diff) > len(candies) // 2:
        return len(candies) // 2
    else:
        return len(diff)


def solution(T):
    diff_candies = set(T)
    if len(diff_candies) < len(T) // 2:
        return len(diff_candies)
    return len(T) // 2

print(candy([3, 4, 7, 7, 6, 6]))
# returns 3
print(candy([80, 80, 1000000000, 80, 80, 80, 80, 80, 80, 123456789]))
# returns 3
print(candy([1, 1, 7, 7, 6, 6]))
# returns 3
print(candy([1, 7, 7, 7]))
# returns 2
print(candy([7, 7, 7, 7]))
# returns 1
