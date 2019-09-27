# https://leetcode.com/problems/rotting-oranges/
# https://leetcode.com/problems/rotting-oranges/solution/


# runtime 56 ms, 92%; memory 13.9 MB, 17%
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = [[]]
        minute = []
        res = 0
        lx = len(grid)-1
        ly = len(grid[0])-1
        oranges = False

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue[0].append((i, j))
                if grid[i][j] == 1:
                    oranges = True

        if not oranges:
            return 0

        while queue:
            curr = queue.pop(0)

            for i in range(len(curr)):
                x, y = curr[i]
                if grid[x][y] == 2:
                    if x < lx and grid[x + 1][y] == 1:
                        grid[x + 1][y] = 2
                        minute.append([x + 1, y])
                    if y < ly and grid[x][y + 1] == 1:
                        grid[x][y + 1] = 2
                        minute.append([x, y + 1])
                    if 0 < x and grid[x - 1][y] == 1:
                        grid[x - 1][y] = 2
                        minute.append([x - 1, y])
                    if 0 < y and grid[x][y - 1] == 1:
                        grid[x][y - 1] = 2
                        minute.append([x, y - 1])

            if minute:
                queue.append(minute)
                minute = []
                res += 1

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1

        return res


# runtime 56 ms, 92%; memory 13.8 MB, 17%
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        res = oranges = 0
        lx = len(grid)-1
        ly = len(grid[0])-1

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append([i, j])
                if grid[i][j] == 1:
                    oranges += 1

        if not oranges:
            return 0

        while queue:
            for i in range(len(queue)):
                x,y = queue.pop(0)
                if grid[x][y] == 2:
                    if x < lx and grid[x + 1][y] == 1:
                        grid[x + 1][y] = 2
                        queue.append([x + 1, y])
                        oranges -= 1
                    if y < ly and grid[x][y + 1] == 1:
                        grid[x][y + 1] = 2
                        queue.append([x, y + 1])
                        oranges -= 1
                    if 0 < x and grid[x - 1][y] == 1:
                        grid[x - 1][y] = 2
                        queue.append([x - 1, y])
                        oranges -= 1
                    if 0 < y and grid[x][y - 1] == 1:
                        grid[x][y - 1] = 2
                        queue.append([x, y - 1])
                        oranges -= 1
            res += 1

        if oranges:
            return -1
        return res - 1


# test case: [[1,2]]  returns 1
