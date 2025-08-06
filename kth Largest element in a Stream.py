# Leetcode 703. Kth Largest Element in a Stream
# Problem Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Category: Heap, Design

import heapq
from typing import List
from collections import defaultdict, deque  

class KthLargest:
    '''
    Input: An integer k and an array of integers nums
    Operations:
    - Use a min-heap to keep track of the k largest elements in the stream
    - Initialize the min-heap with the first k elements of nums
    - For each new element added to the stream, compare it with the smallest element in the heap
    - If the new element is larger, replace the smallest element with the new element
    Output: The kth largest element in the stream after each addition
    T.C: O(N log k) for the initialization where N is the number of elements in nums, and O(log k) for each addition
    S.C: O(k) for the min-heap
    Using a min-heap to efficiently track the kth largest element in a
    '''
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)   # O(n)
        while (len(self.minHeap) > k):
            heapq.heappop(self.minHeap)  # O(log n)

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)  # O(log k)
        elif self.minHeap[0] < val:
            heapq.heappop(self.minHeap)        # O(log k)
            heapq.heappush(self.minHeap, val)  # O(log k)
        return self.minHeap[0]

# Testing the KthLargest class
print("Testing the KthLargest class: ")
kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))   # returns 4
print(kthLargest.add(5))   # returns 5
print(kthLargest.add(10))  # returns 5
print(kthLargest.add(9))   # returns 8
print(kthLargest.add(4))   # returns 8    