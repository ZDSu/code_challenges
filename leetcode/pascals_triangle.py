# https://leetcode.com/problems/pascals-triangle/
# https://leetcode.com/articles/pascals-triangle/


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []

        for i in range(numRows):
            row = [None for _ in range(i + 1)]
            row[0] = 1
            row[-1] = 1
            for j in range(1, len(row) - 1):
                row[j] = res[i-1][j-1] + res[i-1][j]
            res.append(row)

        return res


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        if numRows > 0:
            triangle.append([1])

        for i in range(1, numRows):
            row = [None] * (i + 1)
            row[0] = 1
            row[i] = 1
            if i > 1:
                for j in range(1, i):
                    row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
        return triangle
