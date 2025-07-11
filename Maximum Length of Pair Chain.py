# LeetCode 646. Maximum Length of Pair Chain
# Problem Link: https://leetcode.com/problems/maximum-length-of-pair-chain/
# Category: Dynamic Programming, Recursion, Memoization, Greedy

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n = len(pairs)
        t = [[-1 for _ in range(n+1)] for _ in range(n+1)]

        def solve(idx, prevIdx):
            if idx >= n:
                return 0
            
            if t[idx][prevIdx] != -1:
                return t[idx][prevIdx]
            
            # take
            take = 0
            if prevIdx == -1 or pairs[prevIdx][1] < pairs[idx][0]:
                take = 1 + solve(idx + 1, idx)
            
            # skip
            skip = solve(idx + 1, prevIdx)

            t[idx][prevIdx] = max(take, skip)
            return t[idx][prevIdx]

        return solve(0, -1)