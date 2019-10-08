# https://leetcode.com/problems/brick-wall/
# https://leetcode.com/articles/brick-wall  (Premium)


class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        single = {}
        for row in wall:
            width = 0
            for brick in row[:-1]:
                width += brick
                if width in single:
                    single[width] += 1
                else:
                    single[width] = 1
        if single == {}:
            return len(wall)
        else:
            return len(wall) - max(single.values())
