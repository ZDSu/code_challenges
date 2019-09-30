# https://leetcode.com/problems/missing-ranges/

"""
Missing Ranges
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:
Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]

"""
# test cases:
# [], -3, -1  returns ["-3->-1"]


# P@thr1se solution
# runtime 40 ms, 35%, memory 13.9 MB, 8%
def printNumbers(start, end):
    res = ''
    if start == end:
        res += str(start)
    else:
        temp = ''
        if start < 0:
            temp += str(start) + '->'
        else:
            temp += str(start) + '->'
        if end < 0:
            temp += str(end)
        else:
            temp += str(end)
        res += temp
    return res

class Solution:
    def findMissingRanges(self, nums: List[int], start: int, end: int) -> List[str]:
        res = []
        next = start
        for num in nums:
            if num < start:
                continue
            if num > end:
                res.append(printNumbers(next, end))
                return
            if num > next:
                res.append(printNumbers(next, num-1))
            next = num+1

        if next <= end:
            res.append(printNumbers(next, end))
        return res


# from discussion
# runtime 36 ms, 69%; memory 13.7 MB, 8%
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []

        prev = lower - 1 # so that I can handle case when nums is empty
        for i in range(len(nums)+1):
            current = nums[i] if i < len(nums) else upper+1

            # means, not a continuos range where current number
            # is 1 greater than the last number in the list
            if current > prev+1:
                # now my missing intervals will have number prev+1, current-1
                # I can't take the number already present in the list
                # that means, prev and current can't be part of my answer
                if prev+1 < current-1:
                    res.append(str(prev+1) + "->" + str(current-1))
                else:
                    res.append(str(prev+1))

            prev = current

        return res


# fastest solution
# runtime 32 ms, 91%; memory 13.8 MB, 8%
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        length = len(nums)
        if lower == upper:
            if length == 0:
                return [str(lower)]
            else:
                return []

        if length == 0:
            return [str(lower) + '->' + str(upper)]

        ans = []

        if lower < nums[0] - 1:
            ans.append(str(lower) + '->' + str(nums[0] - 1))
        elif lower == nums[0] - 1:
            ans.append(str(lower))

        for i in range(0, length - 1):
            if nums[i + 1] - nums[i] == 2:
                ans.append(str(nums[i] + 1))
            elif nums[i + 1] - nums[i] > 2:
                ans.append(str(nums[i] + 1) + '->' + str(nums[i + 1] - 1))

        if upper > nums[-1] + 1:
            ans.append(str(nums[-1] + 1) + '->' + str(upper))
        elif upper == nums[-1] + 1:
            ans.append(str(upper))

        return ans


# second fastest solution
# runtime 32 ms, 91%; memory 13.8 MB, 8%
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        # Initialize array with max number
        nums = [lower-1] + nums + [upper+1]
        output = []
        for num1, num2 in zip(nums, nums[1:]):
            if num1+1 >= num2:
                continue
            elif num1+2 == num2:
                output.append(str(num1+1))
            else:
                output.append(f"{num1+1}->{num2-1}")
        return output


# third fastest solution
# runtime 40 ms, 35%; memory 13.6 MB, 8%
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        i=lower
        j=upper
        nums=list(set(nums))
        nums.sort()
        length=len(nums)
        out=[]
        for k in range(0,length):
            if nums[k]!=i:
                j=nums[k]-1
                if i!=j:
                    out.append(str(i)+"->"+str(j))
                else:
                    out.append(str(i))

                i=nums[k]+1
            else:
                i+=1

        if i==upper:
            out.append(str(i))
        elif i<upper:
            out.append(str(i)+"->"+str(upper))

        return out


# from discussion
# runtime 44 ms, 9%; memory 13.8 MB, 8%
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums = [lower-1] + nums + [upper+1]
        res = []

        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 2:
                res.append(str(nums[i]+1))
            elif nums[i+1] - nums[i] > 2:
                res.append(str(nums[i]+1)+'->'+str(nums[i+1]-1))

        return res
