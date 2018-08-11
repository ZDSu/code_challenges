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