"""
Given an interger array, output all the unique pairs that sum up to a specific value k.
Example: pair_sum([1, 3, 2, 2], 4) would return 2 pairs: (1, 3) and (2, 2)

Not quite the same: https://leetcode.com/problems/two-sum/
"""
def pair_sum(arr, k):
    if len(arr) < 2:
        return

    seen = {}
    res = []
    for num in arr:
        target = k - num
        if target in seen:
            res.append((sorted([target, num])))
            seen[target] -= 1
            if seen[target] < 1:
                del seen[target]
        else:
            seen[num] = 0
    return print(res)


# youtube solution
def pair_sum(arr, k):
    if len(arr) < 2:
        return print("Too small")

    seen = set()
    output = set()
    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))

    print('\n'.join(map(str, list(output))))

pair_sum([1, 3, 2, 2], 4)
