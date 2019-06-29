# https://leetcode.com/problems/group-anagrams/
# https://leetcode.com/articles/group-anagrams/


# runtime 84 ms, 89%; memory 15.7 MB, 63%
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        sorts = {}
        count = 0
        for s in strs:
            temp = ''.join(sorted(s))
            if temp not in sorts:
                res.append([s])
                sorts[temp] = count
                count += 1
            else:
                index = sorts[temp]
                res[index].append(s)
        return res
