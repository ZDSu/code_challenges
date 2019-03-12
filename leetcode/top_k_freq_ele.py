# https://leetcode.com/problems/top-k-frequent-elements/
# https://leetcode.com/articles/top-k-frequent-elements/


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        result = []
        for i in range(len(nums)):
            if str(nums[i]) in dict:
                dict[str(nums[i])] += 1
            else:
                dict[str(nums[i])] = 1

        for _ in range(k):
            key = max(dict.items(), key=lambda t: t[1])[0]
            result.append(int(key))
            del dict[key]

        return result


# in progress, try to use new data structure
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or not k:
            return

        count = {}
        res = []

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

#         for i in range(k):
#             res.append(sorted(count.values()))

        print(count.values(), sorted(count.values()))
        print(count.keys(), sorted(count.keys()))
        print(count.items(), sorted(count.items()))
