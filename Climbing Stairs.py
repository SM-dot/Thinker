# Leetcode Problem: 70. Climbing Stairs
# Link: https://leetcode.com/problems/climbing-stairs/
# Difficulty: Easy


'''
Explnanation: 
You are climbing a staircase that has n steps. You can take either 1 step or 2 steps at a time. The task is to determine how many distinct ways you can reach the top of the staircase. 
Time Complexity: O(n) where n is the number of steps. This is because we compute the number of ways to reach each step from 1 to n.
Space Complexity: O(n) for the memoization array or dp array used to store the number
of ways to reach each step. of ways to reach each step.
'''
# Recursion with memoization
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        def helper(n):
            if n <= 2:
                return n
            if dp[n] != -1:
                return dp[n]
            dp[n] = helper(n -1) + helper(n-2)
            return dp[n]
        return helper(n)

# Tabulation
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]