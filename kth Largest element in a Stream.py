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

# REV oct 7, 2025

class KthLargest:
    '''
    Ussually a wya to ratta to know when to use min heap or max heap is to use the opposite of what it is asking. So if it is asking largest use a min heap, if it is asking smallest use a max heap. 

    Another way:
    u know top of min heap has smallest value, to find the largest u want to pop small values so u use min heap

    u know top of max heap has largest value, to fidn the smallest u want to pop large values so u use max heap.

    Ok, here u add to the min heap, if the heap size exceeds k u pop. The top of the heap would have the third/ k largest element cause the bottom in a min heapo has the largets and the top has the smallest. 

    Heaop operations and time compelxity:
    heapify = O(n)
    inserting into a heap = O(logn)
    removing from a heap = O(logn)
    Now let's code!!! 
    '''

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

#REV FEB 3 2026 