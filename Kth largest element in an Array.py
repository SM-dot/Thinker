# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
# Difficulty: Medium
# Category: Array, Sorting, Heap

'''
Explanation:
Given an integer array nums and an integer k, return the kᵗʰ largest element in the array.
Heap Approach:
1. We can use a min-heap to keep track of the k largest elements in the array.
2. First, we convert the list into a heap using heapq.heapify(), which takes O(n) time.
3. Then, we repeatedly pop the smallest element from the heap until the size of the heap is k. Each pop operation takes O(log n) time.
4. Finally, the root of the heap (the smallest element in the heap) will be the k

Time Complexity: O(n + k log n)
Space Complexity: O(1) if we consider the input array as part of the space,

Time complexity of heap: 
heapify: O(n) otherwise O(n) for the heap storage. not counting the input array, since we are modifying it in place.
pop: O(log n) and we do it k times => O(k log n)ᵗʰ largest element in the array.    
'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums
        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)
        
        return heap[0]