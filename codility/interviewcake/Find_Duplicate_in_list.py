"""
Find a duplicate, Space Edition™.

We have a list of integers, where:
1. The integers are in the range 1..n
2. The list has a length of n+1

It follows that our list has at least one integer which appears at least twice. But it may have several duplicates, and each duplicate may appear more than twice.

Write a function which finds an integer that appears more than once in our list. (If there are multiple duplicates, you only need to find one of them.)

We're going to run this function on our new, super-hip MacBook Pro With Retina Display™. Thing is, the damn thing came with the RAM soldered right to the motherboard, so we can't upgrade our RAM. So we need to optimize for space!
"""


# My attempted solution:
def duplicates(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        else:
            seen.add(num)


"""
Gotchas:
We can do this in O(1) space.

We can do this in less than O(n^2) time while keeping O(1) space.

We can do this in O(n*logn) time and O(1) space.

We can do this without destroying the input.

Most O(n*logn) algorithms double something or cut something in half. How can we rule out half of the numbers each time we iterate through the list?

"""

# Breakdown:
# This one's a classic! We just do one walk through the list, using a set to keep track of which items we've seen!

def find_repeat(numbers):
    numbers_seen = set()
    for number in numbers:
        if number in numbers_seen:
            return number
        else:
            numbers_seen.add(number)

    # Whoops--no duplicate
    raise Exception('no duplicate!')

# Bam. O(n) time and ... O(n) space ...
# Right, we're supposed to optimize for space. O(n) is actually kinda high space-wise. Hm. We can probably get O(1)...


# Solution:
# We can "brute force" this by taking each number in the range 1..n and, for each, walking through the list to see if it appears twice.

def find_repeat_brute_force(numbers):
    for needle in range(1, len(numbers)):
        has_been_seen = False
        for number in numbers:
            if number == needle:
                if has_been_seen:
                    return number
                else:
                    has_been_seen = True

    # Whoops--no duplicate
    raise Exception('no duplicate!')

# This is O(1) space and O(n^2) time.
# That space complexity can't be beat, but the time cost seems a bit high. Can we do better?

"""
One way to beat O(n^2) time is to get O(n*logn) time. Sorting takes O(nlgn) time. And if we sorted the list, any duplicates would be right next to each-other!

But if we start off by sorting our list we'll need to take O(n) space to store the sorted list...

...unless we sort the input list in place!
    An in-place algorithm operates directly on its input and changes it, instead of creating and returning a new object. This is sometimes called destructive, since the original input is "destroyed" when it's edited to create the new output.

    Careful: "In-place" does not mean "without creating any additional variables!" Rather, it means "without creating a new copy of the input." In general, an in-place function will only create additional variables that are O(1) space.

    Here are two functions that do the same operation, except one is in-place and the other is out-of-place:

    def square_list_in_place(int_list):
        for index, element in enumerate(int_list):
            int_list[index] *= element

        # NOTE: We could make this function just return, since
        # we modify int_list in place.
        return int_list


    def square_list_out_of_place(int_list):
        # We allocate a new list with the length of the input list
        squared_list = [None] * len(int_list)

        for index, element in enumerate(int_list):
            squared_list[index] = element ** 2

        return squared_list

    Working in-place is a good way to save space. An in-place algorithm will generally have O(1) space cost.

    But be careful: an in-place algorithm can cause side effects. Your input is "destroyed" or "altered," which can affect code outside of your function. For example:

    original_list = [2, 3, 4, 5]
    squared_list  = square_list_in_place(original_list)

    print("squared: %s" % squared_list)
    # Prints: squared: [4, 9, 16, 25]

    print("original list: %s" % original_list)
    # Prints: original list: [4, 9, 16, 25], confusingly!

    # And if square_list_in_place() didn't return anything,
    # which it could reasonably do, squared_list would be None!

    Generally, out-of-place algorithms are considered safer because they avoid side effects. You should only use an in-place algorithm if you're very space constrained or you're positive you don't need the original input anymore, even for debugging.

Okay, so this'll work:
1. Do an in-place sort of the list (for example an in-place merge sort).
2. Walk through the now-sorted list from left to right.
2. Return as soon as we find two adjacent numbers which are the same.
This'll keep us at O(1) space and bring us down to O(nlgn) time.

But destroying the input is kind of a drag--it might cause problems elsewhere in our code. Can we maintain this time and space cost without destroying the input?

Let's take a step back. How can we break this problem down into subproblems?

If we're going to do O(n*logn) time, we'll probably be iteratively doubling something or iteratively cutting something in half. That's how we usually get a "logn". So what if we could cut the problem in half somehow?

Well, binary search [A binary search algorithm finds an item in a sorted list in O(log(n)) time.] works by cutting the problem in half after figuring out which half of our input list holds the answer.

But in a binary search, the reason we can confidently say which half has the answer is because the list is sorted. For this problem, when we cut our unsorted list in half we can't really make any strong statements about which elements are in the left half and which are in the right half.

What if we could cut the problem in half a different way, other than cutting the list in half?

With this problem, we're looking for a needle (a repeated number) in a haystack (list). What if instead of cutting the haystack in half, we cut the set of possibilities for the needle in half?

The full range of possibilities for our needle is 1..n. How could we test whether the actual needle is in the first half of that range (1..n/2) or the second half (n/2+1..n)?

A quick note about how we're defining our ranges: when we take n/2 we're doing integer division, so we throw away the remainder. To see what's going on, we should look at what happens when n is even and when n is odd:
- If n is 6 (an even number), we have  ... so our ranges are 1..3 and 4..6
- If n is 5 (an odd number), ... so our ranges are 1..2 and 3..5
​
So we can notice a few properties about our ranges:
1. They aren't necessarily the same size.
2. They don't overlap.
2. Taken together, they represent the original input list's range of 1..n. In math terminology, we could say their union is 1..n.

So, how do we know if the needle is in the first half or the second half?

Think about the original problem statement. We know that we have at least one repeat because there are n+1 items and they are all in the range 1..n, which contains only n distinct integers.

This notion of "we have more items than we have possibilities, so we must have at least one repeat" is pretty powerful. It's sometimes called the pigeonhole principle. [The pigeonhole principle states that if nn items are put into mm containers, with n > mn>m, then at least one container must contain more than one item. For example, there must be at least two left gloves or two right gloves in a group of three gloves.] Can we exploit the pigeonhole principle to see which half of our range contains a repeat?

Imagine that we separated the input list into two sublists—one containing the items in the range of the first half and the other containing the items in the range of the second half.
​
Each sublist has a number of elements as well as a number of possible distinct integers (that is, the length of the range of possible integers it holds).

Given what we know about the number of elements vs the number of possible distinct integers in the original input list, what can we say about the number of elements vs the number of distinct possible integers in these sublists?
"""

"""
Complexity:
O(1) space and O(n*logn) time.

Tricky as this solution is, we can actually do even better, getting our runtime down to O(n) while keeping our space cost at O(1). The solution is NUTS; it's probably outside the scope of what most interviewers would expect. But for the curious...(here it is)[link]!


Bonus:
This function always returns one duplicate, but there may be several duplicates. Write a function that returns all duplicates.
"""
