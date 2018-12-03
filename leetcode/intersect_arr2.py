# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/


#76 ms, 18.5%
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for num in nums1:
            if num in nums2:
                result.append(num)
                nums2.remove(num)
        return result


# 44 ms, 72%
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums = {}
        result = []
        for num in nums1:
            if num in nums:
                nums[num] += 1
            else:
                nums[num] = 1
        for num in nums2:
            if num in nums:
                if nums[num] > 0:
                    nums[num] -= 1
                    result.append(num)
        return result


# andrii's solution, 40 sec, 99% (but only the second time I ran it. WTH! first time i ran it: 72 ms, 24%)
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        inter = []
        d = {}
        for item in nums2:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        for item in nums1:
            if item in d:
                inter.append(item)
                d[item] -= 1
                if d[item] == 0:
                    del d[item]
        return inter

# test case:  [4,9,5], [9,4,9,8,4]  result: [4,9]


# 68 ms, 28.42%
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        numbers = {}
        
        for each in nums1:
            if each in numbers:
                numbers[each] += 1
            else:
                numbers[each] = 1
        
        for each in nums2:
            if each in numbers:
                result.append(each)
                if numbers[each] == 1:
                    del numbers[each]
                else:
                    numbers[each] -= 1
        return result