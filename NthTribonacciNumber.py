# leetcode problem link: https://leetcode.com/problems/n-th-tribonacci-number/
# leetcode problem: 1137. N-th Tribonacci Number
# category: Dynamic Programming, Recursion, Memoization

# TIME COMPLEXITY: O(N) - we are calculating the tribonacci number for each index from 3 to n once, and each calculation takes O(1) time.
# SPACE COMPLEXITY: O(N) - we are using a dp array of size n + 1 to store the tribonacci numbers for each index from 0 to n.
# without dynamic programming the time comexity would be O(3^N) because for each index we are making 3 recursive calls, and the recursion tree would have a branching factor of 3 and a depth of N.
# The space complexity without dynamic programming would be O(N) due to the recursion stack, where N is the depth of the recursion tree.

# personal noted: relatively straightforward problem, the only thing to be careful about is to handle the base cases for n = 0, 1, 2 to prevent index errors when we try to access dp[i - 1], dp[i - 2], and dp[i - 3] in the recursive function.

class Solution:
    def tribonacci(self, n: int) -> int:
        # Edge cases for very small n to prevent index errors
        if n == 0: return 0
        if n <= 2: return 1

        dp = [-1 for _ in range(n + 1)]
        dp[0], dp[1], dp[2] = 0, 1, 1

        def solve(i):
            # 1. Check if we already calculated this
            if dp[i] != -1:
                return dp[i]
            
            # 2. Recursive step
            dp[i] = solve(i - 1) + solve(i - 2) + solve(i - 3)
            return dp[i]
        
        return solve(n)