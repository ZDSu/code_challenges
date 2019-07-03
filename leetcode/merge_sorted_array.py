# https://leetcode.com/problems/merge-sorted-array/


# runtime 24 ms, 80%; memory 11.8 MB, 32%
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


# runtime 24 ms, 80%; memory 11.7 MB, 67%
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


# runtime 20 ms, 93%; memory 11.7 MB, 70%
# ran again: runtime 20 ms, 93%; memory 11.8 MB, 40%
class Solution:
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

        m -= 1
        n -= 1
        i = len(nums1) - 1

        while n >= 0:
            if nums1[m] > nums2[n] and m >= 0:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
            i -= 1


# runtime 24 ms, 80%; memory 11.8 MB, 33%
class Solution:
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

        m -= 1
        n -= 1
        i = len(nums1) - 1

        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
            i -= 1
        nums1[:n+1] = nums2[:n+1]


# runtime 24 ms, 80%; memory 11.7 MB, 67%
class Solution(object):
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

        # not sure why this code doesn't work, print statements show nums1 is correct but tests fail
        # if m == 0:
        #     nums1 = nums2
        #     return

        for i in range(len(nums1)-1, -1, -1):
            if m > 0 and n > 0:
                if nums1[m-1] > nums2[n-1]:
                    nums1[i] = nums1[m-1]
                    m -= 1
                else:
                    nums1[i] = nums2[n-1]
                    n -= 1
            elif m == 0:
                nums1[0:i+1] = nums2[0:i+1]
            else:
                nums1[0:i+1] = nums1[0:i+1]


# test cases:
# [0], 0, [1], 1  returns [1]
# [1], 1, [], 0  returns [1]
# [2,0], 1, [1], 1 returns [1, 2]
# [4,5,6,0,0,0], 3, [1,2,3], 3  returns [1,2,3,4,5,6]
