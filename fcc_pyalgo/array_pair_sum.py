"""
Given an interger array, output all the unique pairs that sum up to a specific value k.
Example: pair_sum([1, 3, 2, 2], 4) would return 2 pairs: (1, 3) and (2, 2)

Not quite the same: https://leetcode.com/problems/two-sum/
"""
def pair_sum(arr, k):
    if len(arr) < 2:
        return

    seen = {}
    res = set()
    for num in arr:
        target = k - num
        if target in seen:
            res.add(sorted(target, num))
            seen[target] -= 1
            if seen[target] < 1:
                del seen[target]
        else:
            seen[num] = 0
    return res
