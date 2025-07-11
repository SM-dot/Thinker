# LeetCode 1048. Longest String Chain
# Problem Link: https://leetcode.com/problems/longest-string-chain/
# Category: Dynamic Programming, Recursion, Memoization, String, Sorting

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