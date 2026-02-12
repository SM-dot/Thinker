# LeetCode Problem Link: https://leetcode.com/problems/maximum-total-spell-damage/
# LeetCode Problem: 2811. Maximum Total Spell Damage
# Category: Binary Search, Dynamic Programming, Recursion
# Difficulty: Medium

'''
Time complexity: 
for the left bound function we are using binary search so the time compelexity is O(N)
without memoizaation the time complexity is O(2^N) because for each element we have 2 choices, either take it or skip it.
with memoization the time complexity is O(N) because we are storing the results of subproblems in the dp array, and each subproblem is solved only once.
However, for each of the calls we are also calling the logn function or the lower bound fucntion and we are also sorting our inout array 
so the overall time complexity is O(N log N) because of the sorting and the binary search.
Space complexity: O(N) for the dp array used for memoization, where N is the number of unique power values. The space complexity is also O(N) for the frequency map that stores the count of each unique power value. Therefore, the overall space complexity is O(N).

'''
from collections import defaultdict 
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:

        
        def left_bound(power, target): 
            left = 0
            right = len(power) 

            while left < right:
                mid = (left + right)//2
                if power[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        freqMap = defaultdict(int)

        for num in power:
            freqMap[num] += 1
        

        power = sorted(set(power))
        n = len(power)
        dp = [-1 for _ in range(n + 1)]

        def solve(i):
            if i >= n:
                return 0
            
            if dp[i] != -1:
                return dp[i]
            
            take = power[i]*freqMap[power[i]] + solve(left_bound(power, power[i] + 3))
            skip = solve(i + 1)
            dp[i] = max(take, skip)
            return dp[i]
        
        return solve(0)