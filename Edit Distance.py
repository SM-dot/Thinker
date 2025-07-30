# Leetcode 72. Edit Distance
# Problem Link: https://leetcode.com/problems/edit-distance/
# Category: Dynamic Programming

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        We can perform 3 operations for each character:
        i = horse j = ros

        1. Insert (i, j + 1) cause we matched the r
        2. Delete (i + 1, j) we dont actually need to deleet just ignore it and move the pointer ahead 
        3. Replace (i + 1, j + 1) matched it, now move formward

        If the charcters at i == characters at j: i + 1, j + 1

        Handling base cases: 
          i  
        horse = m
           j
        ros = n

        in this case we need to DELETE the remaning characters in the first word so return m - i 
        if j == n: 
            return m - i


         i  
        ab = m
          j
        abcd = n
        here we need to INSERT the characters, so we return n - j 
        if i == m:
            return n - j
        '''
        n = len(word1)
        m = len(word2)
        dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]

        def solve(i, j):
            if i == len(word1):
                return m - j
            if j == len(word2):
                return n - i
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if word1[i] == word2[j]:
                dp[i][j] = solve(i + 1, j + 1)
                return dp[i][j]
            
            insert = 1 + solve(i, j + 1)
            delete = 1 + solve(i + 1, j)
            replace = 1 + solve(i + 1, j + 1)
            dp[i][j] = min(insert, delete, replace)
            return dp[i][j]
        
        return solve(0, 0)