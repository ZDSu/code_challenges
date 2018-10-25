# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i = count = 0
        
        for j in range(1,len(nums)):
            if nums[i] != nums[j] and count < 3:
                i += count
                nums[i] = nums[j]
                count = 0
            count += 1
        return i + 1

# above code fails for test case [0,0,1,1,1,1,2,3,3] which should return [0,0,1,1,2,3,3]

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i = 0
        j = count = 1

        while j < len(nums):
            if nums[i] == nums[j]:
                count += 1
                if count < 3:
                    i += 1
                    nums[i] = nums[j]
                j += 1

            else:
                i += 1
                nums[i] = nums[j]
                count = 1
                j += 1

        if count > 2:
            return i
        else:
            return i + 1
            
# above code fails for test case [1,1,1] which should return [1,1]
          
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i = 0
        j = count = 1

        while j < len(nums):
            if nums[i] == nums[j]:
                count += 1
                if count < 3:
                    i += 1
                    nums[i] = nums[j]
                j += 1

            else:
                i += 1
                nums[i] = nums[j]
                count = 1
                j += 1

        if count > 2 and i < 2:
            return 2
        elif count > 2:
            return i
        else:
            return i + 1

# above code fails for test case [1,2,2,2] which should return [1,2,2]


# very concise solution code found, takes advantage of the fact that it is SORTED!
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i

# someone's explanation of this code: 
# When i = 0, which satisfy the condition " i < 2 or n > nums[i-2] ", the number (index 0) is put to the array(index 0), and i+=1 to the second turn;
# When i = 1, which satisfy the condition " i < 2 or n > nums[i-2] ", the number (index 1) is put to the array(index 1), and i+=1 to the third turn;
# When i = 2,
# First, we suppose that the number (index 2) is bigger than the first two numbers (it must equal or bigger than because the array is already sorted). So for example [1, 2, 3] are still [1, 2, 3].
# Second, we suppose that the number (index 2) is equal as the less 2 indexes number(n == nums[i-2]), which cannot satisfy the condition. So no operation acts. In other words, this turn has no meaning;
# When i = 3,
# First, we suppose that the number (index 3) is bigger than the less 2 indexes number(n > nums[i-2]), so for example [1, 2, 3, 4] are still [1, 2, 3, 4].
# Second, we suppose that the number (index 3) is equal as the less 2 indexes number(n == nums[i-2]), which cannot satisfy the condition. So no operation acts. In other words, this turn has no meaning; So for example [1,4,4,4] are still [1,4,4,4]. And if the number (index 4, we say n) is bigger than 4, will be [1,4,4,n].