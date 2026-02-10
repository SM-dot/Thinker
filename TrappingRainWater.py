# Leetcode: https://leetcode.com/problems/trapping-rain-water/
# Category: Arrays can be solved with stack, dp as well
"""
    This class provides a method to solve the 'Trapping Rain Water' problem.

    Thought Process:
    ----------------
    The idea is to calculate, for each bar, the maximum height of water it can hold.
    The water level at any position depends on the minimum of the highest bars to its left and right.
    
    To avoid recalculating left and right maxima for each index (which would be inefficient),
    we use two auxiliary arrays:
      - left_max[i] stores the maximum height to the left of or at index i.
      - right_max[i] stores the maximum height to the right of or at index i.
    
    Once these are precomputed, we iterate through each index to calculate how much water
    can be trapped above it using:
        trapped_water[i] = min(left_max[i], right_max[i]) - height[i]
    
    The sum of all trapped_water[i] gives the total amount of water trapped.
    """
class Solution:
    def fill_left(self, arr, height):
        for i in range(1, len(arr)):
            arr[i] = max(arr[i - 1], height[i])
        
    def fill_right(self, arr, height):
        for i in range(len(arr) - 2, -1, -1):
            arr[i] = max(arr[i + 1], height[i])

    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n 

        left_max[0] = height[0]
        right_max[n - 1] = height[n-1]

        self.fill_left(left_max, height)
        self.fill_right(right_max, height)
        
        print(left_max)
        print(right_max)
        sum = 0 
        for i in range(1, n):
            sum += min(left_max[i], right_max[i]) - height[i]
        
        return sum 

# Rev feb 9th, 2026