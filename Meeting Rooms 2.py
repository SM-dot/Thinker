# LeetCode Problem: Meeting Rooms II
# Problem Link: https://leetcode.com/problems/meeting-rooms-ii/
# Also available for free at https://www.lintcode.com/problem/919/
# Category: Heap, Sorting, Greedy
import heapq

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

'''
Explanation:
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
Time Complexity: O(n log n) where n is the number of intervals. This is due to the sorting step and the heap operations.
Space Complexity: O(n) in the worst case, which occurs when all meetings overlap and we need a separate room for each meeting, resulting in all end times being stored in the heap.

Visualization:
[[0, 30], [5, 10], [15, 20]]

Room 1: |-------|-------------------------|
Room 2:         |---|-------|
Room 3:                 |-------|   

'''
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda i : i.start)

        if not intervals:
            return 0

        heap = [intervals[0].end]
        meetingRooms = 1
        n = len(intervals)

        for i in range(1, n):
            start = intervals[i].start
            end = intervals[i].end
            if heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
            meetingRooms = max(meetingRooms, len(heap))
        
        return meetingRooms