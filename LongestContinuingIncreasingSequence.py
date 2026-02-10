# LeetCode Problem Link: https://leetcode.com/problems/longest-continuous-increasing-subsequence/
# LeetCode Problem: 674. Longest Continuous Increasing Subsequence
# Category: Array
# Difficulty: Easy

class Solution:
    '''
    Time complexity: O(n), where n is the number of elements in the input array. We traverse the array once to find the longest continuous increasing subsequence.
    Space complexity: O(1), as we are using only a constant amount of extra space
    '''
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums: return 0
        
        length = 1
        maxLen = 1
        
        for i in range(1, len(nums)):
            # Only compare the current number to the one right before it
            if nums[i] > nums[i-1]:
                length += 1
            else:
                length = 1 # Streak broken, restart at 1
            
            # Update maxLen every time length changes
            if length > maxLen:
                maxLen = length
                
        return maxLen
            
