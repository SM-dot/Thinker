# LeetCode Problem Link: https://leetcode.com/problems/last-stone-weight/
# LeetCode Problem: 1046. Last Stone Weight
# Category: Array, Heap (Priority Queue)
# Difficulty: Easy

import heapq
from typing import List


# Explanation: Use a max heap to always get the two largest stones. In Python, we can simulate a max heap by pushing negative values into a min heap.
# Time Complexity: O(n log n), where n is the number of stones. This is because we may need to perform up to n-1 smash operations, and each operation involves two heap pops and possibly one heap push, each taking O(log n) time.
# Space Complexity: O(n) for storing the heap.
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-num for num in stones]
        heapq.heapify(heap)


        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)

            if x != y:
                heapq.heappush(heap, -(y-x))
        
        if heap: 
            return -heap[0]
        return 0