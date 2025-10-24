# LeetCode Problem: Find Peak Element
# Problem Link: https://leetcode.com/problems/find-peak-element/
# Category: Array, Binary Search


'''
Explanation:
There are 2 ways to solve this problem: Linear Scan and Binary Search.
1. Linear Scan:
    - We can iterate through the array and check for each element if it is greater than its neighbors.
    - If it is, we return its index as the peak element.
    - Time Complexity: O(n)
    - Space Complexity: O(1)
2. Binary Search:
    - We can use binary search to find a peak element in logarithmic time.
    - We check the middle element and compare it with its neighbors.
    - If the middle element is greater than its neighbors, we return its index.
    - If the right neighbor is greater, we search in the right half.    
    - If the left neighbor is greater, we search in the left half.
    - Time Complexity: O(log n)
    - Space Complexity: O(1)
Now let's code! :)
'''
# Optimized code: 
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        if n == 1:
            return 0 

        if n >= 2:
            if nums[0] > nums[1]:
                return 0
            if nums[n - 1] > nums[n - 2]:
                return n - 1
        
        l = 0
        r = n - 1

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            
            if nums[mid + 1] > nums[mid - 1]:
                l = mid + 1
            else:
                r = mid - 1
        
        return 0

# Brute Force Linear Scan:
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        if n == 1:
            return 0 
            
        if n >= 2:
            if nums[0] > nums[1]:
                return 0
            if nums[n - 1] > nums[n - 2]:
                return n - 1
            

        for i in range(1, n - 1):
            if nums[i] > nums[ i - 1] and nums[i] > nums[i + 1]:
                return i
        return -1
    