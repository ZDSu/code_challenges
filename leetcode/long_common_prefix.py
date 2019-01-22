# https://leetcode.com/problems/longest-common-prefix/
# https://leetcode.com/articles/longest-common-prefix/


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0 or strs[0] == '':
            return ''
        prefix = ''
        for i in range(len(strs[0])):
            prefix += strs[0][i]
            for each in strs:
                if each.startswith(prefix):
                    continue
                else:
                    return prefix[:-1]
        return prefix


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        
        prefix = ''  
        for i in range(len(strs[0])):
            curr = strs[0][i]
            for j in range(len(strs)):
                if (i > len(strs[j]) - 1) or (curr != strs[j][i]):
                    return prefix
            prefix += curr
        return prefix


# test cases: 
# ["aa","a"]   returns "a"
# [""]   returns ""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        prefix = ''
        for i in range(len(strs[0])):
            prefix += strs[0][i]
            for word in strs:
                if (i > len(word) - 1) or (word[i] != prefix[i]):
                    return prefix[:-1]
        return prefix


# best solution
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        shortest = min(strs)
        for i in range(len(shortest)):
            for word in strs:
                if word[i] != shortest[i]:
                    return shortest[:i]
        return shortest