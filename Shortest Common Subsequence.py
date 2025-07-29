# Leetcode 1092. Shortest Common Supersequence
# Problem Link: https://leetcode.com/problems/shortest-common-supersequence/
# Category: Dynamic Programming 

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        '''
        Input: Two strings str1 and str2
        Operations:     
        - Use Dynamic Programming to find the length of the longest common subsequence (LCS) between str1 and str2
        - Construct the shortest common supersequence (SCS) by combining characters from both strings while ensuring that the LCS is preserved
        Output: The shortest common supersequence of str1 and str2
        T.C: O(N * M) where N is the length of str1 and M is the length of str2
        S.C: O(N * M) for the DP table
        Using Dynamic Programming to find the shortest common supersequence
        '''
        n = len(str1)
        m = len(str2)

        t = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
        
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 or j == 0: 
                    t[i][j] = i + j 
                elif str1[i-1] == str2[j - 1]:
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = 1 + min(t[i-1][j], t[i][j-1])
        
        scs = []
        i = n
        j = m 
        while (i > 0 and j > 0):
            if str1[i-1] == str2[j-1]:
                scs.append(str1[i-1])
                i -= 1
                j -= 1
            else:
                if t[i-1][j] < t[i][j - 1]:
                    scs.append(str1[i-1]) 
                    i -= 1
                else:
                    scs.append(str2[j-1]) 
                    j -= 1
        
        while i > 0:
            scs.append(str1[i - 1])
            i -= 1
        
        while j > 0:
            scs.append(str2[j-1])
            j -= 1
        
        result = ''.join(reversed(scs))
        return result 



