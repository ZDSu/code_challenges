# https://leetcode.com/problems/merge-sorted-array/description/


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return
        nums1[m:] = nums2
        nums1.sort()


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        idx = m + n - 1
        while n > 0:
            if m > 0 and nums1[m - 1] > nums2[n - 1]:
                nums1[idx] = nums1[m - 1]
                m -= 1
            else:
                nums1[idx] = nums2[n - 1]
                n -= 1
            idx -= 1


# test cases:
# [0], 0, [1], 1  returns [1]
# [2,0], 1, [1], 1 returns [1, 2]