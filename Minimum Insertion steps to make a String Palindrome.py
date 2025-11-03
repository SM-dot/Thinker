# Leetcode 1312. Minimum Insertion Steps to Make a String Palindrome
# Problem Link: https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
# Category: Dynamic Programming

# 3 approaches:
# 1. Bottom Up DP
# 2. Recursive + Memoization
# 3. Recursive

# BOTTOM UP DP
class Solution:
    def minInsertions(self, s: str) -> int:
        '''
        Input: A string s
        Operations:
        - Use Dynamic Programming to find the minimum number of insertions required to make the string a palindrome
        - Create a DP table where t[i][j] is the minimum number of insertions needed to make the substring s[i:j+1] a palindrome
        - Iterate through all possible substrings of length L and update the DP table
        Output: The minimum number of insertions required to
        make the entire string a palindrome
        T.C: O(N^2) where N is the length of the string s
        S.C: O(N^2) for the DP table
        Using Dynamic Programming to find the minimum insertions to make a string palindrome
        '''
        n = len(s)
        # t[i][j] = minimum number of insertions to make i..j palindrome
        t = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        '''
        Cause substrings of length 1 will have 0 insertions
        for i in range(n):
            t[i][i] = 0
        '''
        
        for L in range(2, n + 1):
            for i in range(0, n-L+1):
                j = L + i - 1

                if s[i] == s[j]:
                    t[i][j] = t[i + 1][j - 1]
                else:
                    t[i][j] = 1 + min(t[i +1][j],t[i][j-1])

        return t[0][n-1]

# RECURSION + MEMOIZATION
class Solution:
    def minInsertions(self, s: str) -> int:
        '''
        Recursive + Memoization
        mbadm
        i.  j
        if characters are equal means we do not need to insert, just check the middle string.
        if characters not equal:
            2 cases:
            1. insert the j character at i and move ahead i, j - 1
            2. insert the i character at j and move ahead i + 1, j
        # T.C: O(N^2) where N is the length of the string s
        # S.C: O(N^2) for the dp table + recursive stack space
        Using a recursive approach with memoization to find the minimum insertions to make a string palindrome
        '''
        n = len(s)
        t = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

        def solve(i, j):
            if i >= j:
                return 0
            
            if t[i][j] != -1:
                return t[i][j]
            if s[i] == s[j]:
                t[i][j] = solve(i + 1, j - 1)
                return t[i][j]
            else:
                leftCheck = 1 + solve(i + 1, j)
                rightCheck = 1 + solve(i, j - 1)
                t[i][j] = min(leftCheck, rightCheck)
                return t[i][j]
        
        return solve(0, len(s) - 1)
    
# RECURSION
class Solution:
    def minInsertions(self, s: str) -> int:
        '''
        Simple recursive solution
        mbadm
        i.  j
        if characters are equal means we do not need to insert, just check the middle string.
        if characters not equal:
            2 cases:
            1. insert the j character at i and move ahead i, j - 1
            2. insert the i character at j and move ahead i + 1, j
        # T.C: O(2^N) where N is the length of the string s
        # S.C: O(N) for the recursive stack space
        Using a recursive approach to find the minimum insertions to make a string palindrome
        '''
        def solve(i, j):
            if i >= j:
                return 0
            
            if s[i] == s[j]:
                return solve(i + 1, j - 1)
            
            else:
                leftCheck = 1 + solve(i + 1, j)
                rightCheck = 1 + solve(i, j - 1)
                return min(leftCheck, rightCheck)
        
        return solve(0, len(s) - 1)