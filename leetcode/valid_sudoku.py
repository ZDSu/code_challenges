# https://leetcode.com/problems/valid-sudoku/
# https://leetcode.com/articles/valid-sudoku/ (subscription only)


# runtime: 52 ms, 55%; memory 10.9 MB, 5%
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            row_nums = set()
            for column in row:
                if column == '.':
                    continue
                if column in row_nums:
                    return False
                row_nums.add(column)

        for i in range(9):
            col_nums = set()
            for j in range(len(board)):
                if board[j][i] == '.':
                    continue
                if board[j][i] in col_nums:
                    return False
                col_nums.add(board[j][i])

        grid_nums1 = set()
        grid_nums2 = set()
        grid_nums3 = set()
        for i in range(3):
            for j in range(3):
                if board[i][j] == '.':
                    continue
                if board[i][j] in grid_nums1:
                    return False
                grid_nums1.add(board[i][j])
            for k in range(3,6):
                if board[i][k] == '.':
                    continue
                if board[i][k] in grid_nums2:
                    return False
                grid_nums2.add(board[i][k])
            for j in range(6,9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in grid_nums3:
                    return False
                grid_nums3.add(board[i][j])

        grid_nums1 = set()
        grid_nums2 = set()
        grid_nums3 = set()
        for i in range(3,6):
            for j in range(3):
                if board[i][j] == '.':
                    continue
                if board[i][j] in grid_nums1:
                    return False
                grid_nums1.add(board[i][j])
            for k in range(3,6):
                if board[i][k] == '.':
                    continue
                if board[i][k] in grid_nums2:
                    return False
                grid_nums2.add(board[i][k])
            for j in range(6,9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in grid_nums3:
                    return False
                grid_nums3.add(board[i][j])

        grid_nums1 = set()
        grid_nums2 = set()
        grid_nums3 = set()        
        for i in range(6,9):
            for j in range(3):
                if board[i][j] == '.':
                    continue
                if board[i][j] in grid_nums1:
                    return False
                grid_nums1.add(board[i][j])
            for k in range(3,6):
                if board[i][k] == '.':
                    continue
                if board[i][k] in grid_nums2:
                    return False
                grid_nums2.add(board[i][k])
            for j in range(6,9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in grid_nums3:
                    return False
                grid_nums3.add(board[i][j])
        return True


# Custom test cases:
# Example 1 (True): [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

# Example 2 (False; col 1 and grid 1 are both invalid): [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

# Row 1 invalid: [["5","3",".",".","7",".",".","5","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".","7","5"],[".",".",".",".","8",".",".","7","9"]]

# Row 9 invalid: [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".","7","5"],["7",".",".",".","8",".",".","7","9"]]

# Grid 9 invalid: [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".","7","5"],[".",".",".",".","8",".",".","7","9"]]
