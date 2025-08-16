# LeetCode 213. House Robber II
# Problem Link: https://leetcode.com/problems/house-robber-ii/
# Category: Dynamic Programming


class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Input: List of non-negative integers representing the amount of money in each house arranged in a circle
        Operations: 
           - Since the houses are in a circle, the first and last houses cannot be robbed together
           - Break the problem into two scenarios: robbing from house 0 to n-2 and robbing from house 1 to n-1
           - Use dynamic programming to decide whether to rob a house or skip it in each scenario
           - Maintain a dp array where dp[i] represents the maximum amount that can be robbed up to house i
           - For each house, decide to rob it (add its value to dp[i-2]) or skip it (take dp[i-1])
        Output: Maximum amount of money that can be robbed without robbing two adjacent houses
        T.C: O(N) where N is the number of houses
        S.C: O(N) for the dp array
        TLDR:
        -> either rob house 0 till n - 1
        -> or rob 1 till nth house 

        func(start, ending):
            -> 2 decisions can be made for each house
                => rob the house
                => skip the house
            -> maximum profit in robbing the houses from the starting to the ending house
        '''
        n = len(nums)

        if n == 0:
            return -1
        
        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums[0], nums[1])

        def solve(start, end):
            dp = [-1 for i in range(n + 1)]
            dp[start] = nums[start]
            dp[start + 1] = max(nums[start], nums[start + 1])

            for i in range(start + 2, end + 1):
                rob = nums[i] + dp[i-2]
                skip = dp[i-1]
                dp[i] = max(rob, skip)
            
            return dp[end]
        
        # case where we can rob from houses 0 to n-1
        case1 = solve(0, n -2)
        # case where we can rob from houses 1 to n
        case2 = solve(1, n-1)

        return max(case1, case2)