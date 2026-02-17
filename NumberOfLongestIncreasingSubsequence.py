# LeetCode Problem Link: https://leetcode.com/problems/number-of-longest-increasing-subsequence/
# LeetCode Problem: 673. Number of Longest Increasing Subsequence
# Category: Array, Dynamic Programming
# Difficulty: Medium


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        count = [1 for _ in range(n + 1)]
        dp = [1 for _ in range(n + 1)]
        maxLIS = 1

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 == dp[i]:
                        count[i] += count[j]
                    elif dp[j] + 1 > dp[i]:
                        count[i] = count[j]
                        dp[i] = dp[j] + 1
            if dp[i] > maxLIS:
                maxLIS = dp[i]
        answer = 0
        for i in range(n):
            if dp[i] == maxLIS:
                answer += count[i]
        return answer 
 
        
        