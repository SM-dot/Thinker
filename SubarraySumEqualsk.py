# LeetCode Problem Link: https://leetcode.com/problems/subarray-sum-equals-k/
# LeetCode Problem: 560. Subarray Sum Equals K
# Category: Array, Hash Table, Prefix Sum
# Difficulty: Medium


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        we want to build subarrays, u would think dp might be the way to go about it but there is an easier way to do so. Think of it like two sum 

        You want to find all the subarrays that sum to k. 
        if previously u have seen a subarray of length 6, and ur target is 10. Your curr num is 4. SO u found a subarray whose sum equals k.

        Main goal is to get the sum of the window, check if another window till that sum exists and then subtract it and to the result. 

        See prev submission for better explanation. 

        O(n) solution, now let's code! 
        '''
        result = 0
        n = len(nums)
        currSum = 0
        mp = {}
        mp[0] = 1

        for i in range(n):
            currSum += nums[i]
            diff = currSum - k #REMEMBER THIS: IT IS CURRSUM - K AND NOT K - CURRSUM CAUSE U ARE LOOKING FOR A PREV SUBARRAY SO ESSENTIALLY THE EQUATION BECOMES CURRSUM - PREVSUM = K, U DONT KNOW PREV SUM SO U DO CURRSUM - K IN THE EQUATION. 
            if diff in mp:
                result += mp[diff]
            mp[currSum] = mp.get(currSum, 0) + 1
        
        return result 