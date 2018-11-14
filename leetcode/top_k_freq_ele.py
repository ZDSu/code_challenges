# https://leetcode.com/problems/top-k-frequent-elements/description/


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