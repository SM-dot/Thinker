# LeetCode 646. Maximum Length of Pair Chain
# Problem Link: https://leetcode.com/problems/maximum-length-of-pair-chain/
# Category: Dynamic Programming, Recursion, Memoization, Greedy

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        '''
        Recursion + Memoization code, TC: O(N^2), SC: O(N^2) + O(N) recursion stack
        Sort the pairs based on the first element of each pair
        For each pair, we have 2 choices - take or skip
        If taking, check if the current pair can be chained with the previous pair taken
        If skipping, simply move to the next pair
        
        Can be solved more optimallty using Greedy approach - TC: O(N log N), SC: O(1)
        '''
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