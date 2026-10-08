# LeetCode 1048. Longest String Chain
# Problem Link: https://leetcode.com/problems/longest-string-chain/
# Category: Dynamic Programming, Recursion, Memoization, String, Sorting

# Recursion + Memoization
# T.C: O(N^2 * L) L is the length of the longest word
# S.C: O(N^2) + O(N) recursion stack
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = len)
        n = len(words)
        t = [[-1 for _ in range(n+1)] for _ in range(n + 1)]

        def isPredecessor(wordA, wordB):
            if len(wordB) != len(wordA) + 1:
                return False
            
            i = 0
            j = 0 
            n = len(wordA)
            m = len(wordB)
            while i < n and j < m:
                if wordA[i] == wordB[j]:
                    i += 1
                j += 1
            return i == n

        def solve(idx, prevIdx):
            if idx >= n:
                return 0 
            
            if t[idx][prevIdx] != -1:
                return t[idx][prevIdx]
            
            # take 
            take = 0 
            if prevIdx == -1 or isPredecessor(words[prevIdx], words[idx]):
                take = 1 + solve(idx + 1, idx)
            
            #skip
            skip = solve(idx + 1, prevIdx)

            t[idx][prevIdx] = max(take, skip)
            return t[idx][prevIdx]
        
        return solve(0, -1)

# Bottom Up DP
# T.C: O(N^2 * L) L is the length of the longest word
# S.C: O(N) from dp array
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        n = len(words)
        t = [1 for i in range(n+1)]
        # longest chain till index i 

        def isPredecessor(wordA, wordB):
            if len(wordB) != len(wordA) + 1:
                return False
            
            i=j=0
            n = len(wordA)
            m = len(wordB)
            while i < n and j < m:
                if wordA[i] == wordB[j]:
                    i += 1
                j += 1
            return i==n

        maxLIS = 1
        for i in range(n):
            for j in range(0, i):
                if isPredecessor(words[j], words[i]):
                    t[i] = max(t[i], t[j] + 1)
                    maxLIS = max(maxLIS, t[i])
        return maxLIS

# REV Aug 11th, 2025 

class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        '''
        So if we did LIS, what we were doing was checking the words over and over again, instead of checking if each word is a predecessor what we can do is take a better approach at this. 

        We can store all the words in a hashmap and avoid the O(n sqaure setting). So we basically say of we drop a character is that in our dp and what is the max subsequence that exists with it and we add that to the number of subsequences. 

        Now lets code 
        '''
        words.sort(key = lambda x: len(x))
        dp = {}
        longest = 1 
        
        for word in words: 
            currMax = 1

            for k in range(len(word)):
                new_word = word[:k] + word[k + 1:]
                if new_word in dp:
                    currMax = max(currMax, 1 + dp[new_word])
            
            dp[word] = currMax
            longest = max(longest, dp[word])
        
        return longest 
