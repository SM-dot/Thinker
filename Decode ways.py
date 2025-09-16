# Leetcode Link: https://leetcode.com/problems/decode-ways/
# Leetcode Problem: Decode Ways
# Category: String, Dynamic Programming, Recursion, Memoization
# Difficulty: Medium

'''
Explanation:
To solve the problem of decoding a string of digits into letters, we can use a recursive approach with memoization to optimize it. The idea is to explore two main options at each step:
1. Decode the current single digit (if it's not '0') and move to the next digit.
2. Decode the current and the next digit together (if they form a valid number between
10 and 26) and move two digits ahead.

time Complexity: O(n), where n is the length of the string s. Each position in the string is processed once.
space Complexity: O(n), for the memoization array and the recursion stack.
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1 for i in range(n)]
        def solve(i):
            if i == n:
                return 1 # found a valid sequence
            
            if dp[i] != -1:
                return dp[i]

            if s[i] == '0':
                dp[i] = 0 # not a valid path 
                return dp[i]
            
            only_ith_char = solve(i + 1) # taking only the ith character 267 -> 2, 67
            # taking ith and (i+1)th character together 267 -> 26, 7
            ith_char_and_next_char = 0

            if i + 1 < n:
                if s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6'):
                    ith_char_and_next_char = solve(i + 2)
            
            dp[i] = only_ith_char + ith_char_and_next_char
            return dp[i]
        
        return solve(0)
