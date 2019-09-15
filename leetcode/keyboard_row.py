# https://leetcode.com/problems/keyboard-row/


# runtime 40 ms, 28%; memory 13.9 MB, 7%
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set('QqWwEeRrTtYyUuIiOoPp')
        row2 = set('AaSsDdFfGgHhJjKkLl')
        row3 = set('ZzXxCcVvBbNnMm')

        res = []
        for word in words:
            if word[0] in row1:
                row = row1
            elif word[0] in row2:
                row = row2
            else:
                row = row3
            all = True
            for letter in word:
                if letter not in row:
                    all = False
            if all:
                res.append(word)
        return res


# someone else's solution
# runtime 36 ms, 66%; memory 13.7 MB, 7%
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set('QqWwEeRrTtYyUuIiOoPp')
        row2 = set('AaSsDdFfGgHhJjKkLl')
        row3 = set('ZzXxCcVvBbNnMm')

        ans = []
        row1_count = row2_count = row3_count = 0

        for w in words:
            for i in w:
                if i in row1:
                    row1_count+=1
                elif i in row2:
                    row2_count+=1
                elif i in row3:
                    row3_count+=1
            if row1_count==len(w) or row2_count==len(w) or row3_count==len(w):
                ans.append(w)
            row1_count = row2_count = row3_count = 0

        return ans


# test case:
# ["a","b"]  returns ["a","b"]
