# https://leetcode.com/problems/string-compression/
# https://leetcode.com/articles/string-compression/


class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) == 1:
            return

        j = 0
        for i in range(len(chars)):
            if chars[i] != chars[j]:
                chars[j + 1] = str((i - j))
                j += 2
        chars[j + 1] = str((len(chars) - j))
        return j + 2

# testing
# ["a","a","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c"] returns ["a","2","b","1","2","c","2"]
# ["a","a","b","b","c","c","c"]   returns ["a","2","b","2","c","3"]

# need to account for char > 9 and if len(chars) < len(compressed)