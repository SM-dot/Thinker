# leetcode 516. Longest Palindromic Subsequence
# Problem Link: https://leetcode.com/problems/longest-palindromic-subsequence/
# Category: Dynamic Programming, String
# 3 approaches: 
# 1. Recursive
# 2. Recursive + Memoization
# 3. Bottom Up DP


# RECURSION + MEMOIZATION
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
        Case 1: if the characters at the end are the same then check the inner characters s[i] == s[j]
        answer = 2 + i + 1, j - 1
        we add 2 as 2 characters matched and can be used to form a subsequence

        Case 2: characters at the end are not same s[i] != s[j]
        then 
        1. i + 1, j check 
        2. i, j - 1 check
        store the max 
        Let's code!
        T.C: O(N^2) where N is the length of the string s
        S.C: O(N^2) for the dp table + recursive stack space
        '''
        n = len(s)
        t = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
        # t[i][j] = tells us the LPS from i to j 

        def solve(i, j):
            if i > j:
                return 0
            
            if i == j:
                return 1
            
            if t[i][j] != -1:
                return t[i][j]
            
            if s[i] == s[j]:
                t[i][j] =  2 + solve(i + 1, j - 1)
                return t[i][j]
            else:
                t[i][j] =  max(solve(i + 1, j), solve(i, j - 1))
                return t[i][j]

        
        return solve(0, n - 1)
    
# RECURSION 
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
        Recursive
        Case 1: if the characters at the end are the same then check the inner characters s[i] == s[j]
        answer = 2 + i + 1, j - 1
        we add 2 as 2 characters matched and can be used to form a subsequence

        Case 2: characters at the end are not same s[i] != s[j]
        then 
        1. i + 1, j check 
        2. i, j - 1 check
        store the max 
        Let's code!
        T.C: O(2^N) where N is the length of the string s
        S.C: O(N) - recursion stack space
        Using a recursive approach to find the longest palindromic subsequence
        '''
        n = len(s)

        def solve(i, j):
            if i > j:
                return 0
            
            if i == j:
                return 1
            
            if s[i] == s[j]:
                return  2 + solve(i + 1, j - 1)
            else:
                return max(solve(i + 1, j), solve(i, j - 1))

        
        return solve(0, n - 1)

# BOTTOM UP APPROACH
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
        Following the blueprint for palindromic substring, we can make palindromic subsequence from it at well

        This is a bottom up approach 
        T.C: O(N^2) where N is the length of the string s
        S.C: O(N^2) for the DP table
        Using Dynamic Programming to find the longest palindromic subsequence
        '''
        n = len(s)
        t = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        # t[i][j] = tells us the LPS from i to j 
        # thus the longest would be 0 to n - 1 and that's what we return 

        # length 1 subsequences (3, 3), (2, 2) etc
        for i in range(n):
            t[i][i] = 1

        # 0 and 1 already figured thus starting from 2 
        for L in range(2, n + 1):
            for i in range(n - L + 1):
                j = L + i - 1
                
                if s[i] == s[j]:
                    t[i][j] = 2 + t[i + 1][j - 1]
                else:
                    t[i][j] = max(t[i + 1][j], t[i][j - 1])
        
        return t[0][n - 1]

