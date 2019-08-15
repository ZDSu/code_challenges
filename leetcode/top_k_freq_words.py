# https://leetcode.com/problems/top-k-frequent-words/
# https://leetcode.com/problems/top-k-frequent-words/solution/


# runtime 44 ms, 54%; memory 11.8 MB, 52%
import heapq
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = collections.Counter(words)
        maxheap = [(-f, w) for w, f in count.items()]
        heapq.heapify(maxheap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(maxheap)[1])
        return res
