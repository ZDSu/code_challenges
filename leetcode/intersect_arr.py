# https://leetcode.com/problems/intersection-of-two-arrays/description/


class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1.intersection(nums2))


# runtime 40 ms, 74%; memory 13.2 MB, 5%
class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []

        ans = set()
        nums1 = set(nums1)
        for num in nums2:
            if num in nums1:
                ans.add(num)
        return list(ans)
