# https://leetcode.com/problems/meeting-rooms/description/

"""
Meeting Rooms
Given an array of meeting time intervals consisting of start and end times [[s1,e1], [s2,e2], ...] (si < ei), determine if a person could attend all meetings.

Example 1:
Input: [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: [[7,10],[2,4]]
Output: true
"""

# runtime 100 ms, 12%; memory 17.3 MB, 8%
import heapq
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True

        intervals.sort(key = lambda x : x[0])
        pq = []
        heapq.heappush(pq, intervals[0][1])

        for interval in intervals[1:]:
            if interval[0] < pq[0]:
                return False
            heapq.heappop(pq)
            heapq.heappush(pq, interval[1])
        return True


# runtime 96 ms, 19%; memory 17.1 MB, 8%
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        l1 = []
        for i in intervals:
            for j in i:
                l1.append(j)
        l1.sort()
        l2 = []
        intervals.sort()
        for i in intervals:
            for j in i:
                l2.append(j)
        return l1 == l2


# runtime 92 ms, 48%; memory 17.3 MB, 8%
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if intervals == []:
            return True

        intervals = sorted(intervals, key = lambda x:x[0])
        prev = intervals[0]

        for lst in intervals[1:]:
            if lst[0] < prev[1]:
                return False
            prev = lst
        return True


# runtime 92 ms, 48%; memory 17.3 MB, 8%
# import heapq
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True

        heapq.heapify(intervals)
        end = heapq.heappop(intervals)[1]

        while len(intervals) > 0:
            meeting = heapq.heappop(intervals)
            if meeting[0] < end:
                return False
            end = meeting[1]

        return True
