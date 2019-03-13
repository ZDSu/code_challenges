# https://leetcode.com/problems/top-k-frequent-elements/
# https://leetcode.com/articles/top-k-frequent-elements/


# runtime 252 ms, 5%; memory 15.8 MB, 8%
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


# runtime 56 ms, 43%; memory 16 MB, 8%
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []

        count = collections.Counter(nums)
        res = collections.Counter(count).most_common(k)

        for i in range(len(res)):
            res[i] = res[i][0]

        return res
