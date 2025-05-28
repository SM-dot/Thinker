# Link: https://leetcode.com/problems/longest-common-subsequence/
# Category: DP 
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        t = [[-1 for j in range(m + 1)] for i in range(n + 1)]

        def lcs(x, y, n, m):
            # if "", "fksdhb" then common subzequence length = 0 as common is ""
            if n == 0 or m == 0:
                return 0 
            
            # checking if we have already computed the answer 
            if t[n][m] != -1:
                return t[n][m]
            
            # the letters are the same
            if x[n-1] == y[m-1]:
                t[n][m] = 1 + lcs(x, y, n - 1, m - 1)
                return t[n][m]
            else:
                # letters are not same
                # once take x full and y -1, next take y full and x-1 see whichver path gives better results
                t[n][m] = max(lcs(x, y, n - 1, m), lcs(x, y, n, m - 1))
                return t[n][m]
        
        lcs(text1, text2, n, m)
        return t[n][m]
            
