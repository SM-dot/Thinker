# LeetCode Problem: 167. Two Sum II - Input Array Is Sorted
# Problem Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Category: Array, Two Pointers

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right: 
            total = numbers[left] + numbers[right]
            if total == target: 
                return [left + 1, right + 1]
            
            if total < target: 
                left += 1
            
            if total > target:
                right -=1 
        
        return []