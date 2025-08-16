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
            

# Printing The Sequence 
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        t = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
        # Tells you the length of the longest subsequence when length of text1 is n and length of text2 is m 
        # m + 1, n + 1 cause the answer is at m,n

        # the first row and column will be 0
        # Because if "" and "befkhjwbE" then LCS is 0
        # or if "FGHWADCL" and "" then also LCS is 0

        for row in range(n + 1):
            t[row][0] = 0
        
        for col in range(m + 1):
            t[0][col] = 0

        # starting from 1, cause have already filled out 0, 0 
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i-1] == text2[j-1]:
                    # from the recursive code we should have filled out 1 + t[i+1][j+1] but notice that's some garbage value rn cause we havent fixed it, instead build it from the back thus doing i-1, j-1
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
        
        # Printing the subsequence 
        # Basically only print when u know the characters match in the substring
        # If they do not, u move up based on the cell info 
        # If they do you move up diagonally
        # you build the result from the right bottom corner
        # thus reverse the string in the end 
        LCS = []
        i = n
        j = m 
        while ( i > 0 and j > 0):
            if text1[i-1] == text2[j-1]:
                LCS.append(text1[i-1])
                i -= 1
                j -= 1
            else:
                if (t[i-1][j] > t[i][j-1]):
                    i -= 1
                else:
                    j -= 1       
        LCS.reverse()
        print(LCS)
        return t[n][m]