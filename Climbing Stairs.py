# Leetcode Problem: 70. Climbing Stairs
# Link: https://leetcode.com/problems/climbing-stairs/
# Difficulty: Easy
# Category: Dynamic Programming


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

# Min Cost Climbing Stairs (Leetcode 746)
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        '''
        Read the question carefully. See the wroding, start from 0th or the first step. You want to go ahead and move one or two steps and add that to the cost. You get the minimum cost from 1 or 2 steps in the future. That is what the recursion solution returns. 

        If you think about the memoizaed solution that is basically saying that, if I reach this index step I would have reached either from step 1 or step 2. So in that case, go aheaf and tell me which step took the least cost, I will add that with my current cost and stroe it. So essentialy each cost in the array tells us the minimum cost to get to that step. In the end you return the minimum of either last or second alst step cause if u take one or two steps from there there is no additional cost being added and you have reached the end. 

        Purely recursive solution would have a time complexitu of 2**n because at each step you can take 1 or 2 steps. If you do dp then O(n). If you do bottom up then it is still O(n). The bottom up solution is kind of beautiful if u think about it. It is super simple clean and beautiful. 
        '''

        n = len(cost)

        if n <= 2:
            return min(cost)

        for i in range(2, n):
            cost[i] = cost[i] + min(cost[i - 1], cost[i - 2])
        
        return min(cost[n - 1], cost[n - 2])
