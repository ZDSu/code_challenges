# https://leetcode.com/problems/task-scheduler/
# https://leetcode.com/problems/task-scheduler/solution/

# also see p@thrise dr0pbox prog_ses for their solution

"""
Task Scheduler
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

Note:
1. The number of tasks is in the range [1, 10000].
2. The integer n is in the range [0, 100].
"""
class Solution:
    def leastInterval(self, tasks: List[str], cooldown: int) -> int:
        pass
#         see pathrise dropbox for solution


# (not mine)
# runtime 676 ms, 31%; memory 14.1 MB, 5%
import heapq
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pq = []
        for key, value in Counter(tasks).items():
            heapq.heappush(pq, (-1 * value, key))

        total_time = 0
        while pq:
            i, temp = 0, []
            while i <= n:
                total_time += 1
                if pq:
                    x, y = heapq.heappop(pq)
                    if x != -1:
                        temp.append((x + 1, y))
                if not pq and not temp:
                    break
                else:
                    i += 1
            for item in temp:
                heapq.heappush(pq, item)

        return total_time


# (not mine)
# runtime 688 ms, 28%; memory 14.1 MB, 5%
from heapq import heappush, heappop
from collections import Counter
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        curr_time, h = 0, []
        for k,v in Counter(tasks).items():
            heappush(h, (-1*v, k))
        while h:
            i, temp = 0, []
            while i <= n:
                curr_time += 1
                if h:
                    x,y = heappop(h)
                    if x != -1:
                        temp.append((x+1,y))
                if not h and not temp:
                    break
                else:
                    i += 1
            for item in temp:
                heappush(h, item)
        return curr_time
