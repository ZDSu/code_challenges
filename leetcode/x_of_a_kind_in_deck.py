# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
# https://leetcode.com/articles/x-of-a-kind-in-a-deck-of-cards/


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = {}
        for num in deck:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
