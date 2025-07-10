# LeetCode 1911. Maximum Alternating Subsequence Sum
# Problem Link: https://leetcode.com/problems/maximum-alternating-subsequence-sum/
# Category: Dynamic Programming, Recursion, Memoization

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        '''
        Brute force: 
        find all subsequences(2^n time), for each subsequence find the alternating sum (n time)
        T.C: O(2^N * N)

        For this problem we can draw a tree diagram => can use DP
        for each element in the array we can either take it in the subsequence or skip it. 

        for each element - if taking - we need to check and see if the index is even or odd and then add it. When we move tot he next element the sign/ task of addind or subtracting would be the opposite of what we just carried out.

        for each element - if skipping - we simply compute the answer for the remaning elements. Since we did not take the element the signage/ taks of adding or subtracting remains the same as the index was not changed cause we skipped.

        Recursion Solution (will not submit on leetcode - TLE)
        T.C: O(2^N)
        S.C: O(N) - recursion stack
        '''
        n = len(nums)

        def solve(idx, flag):
            # If we have considered all elements
            if idx >= n:
                return 0
            
            skip = solve(idx + 1, flag)
            val = nums[idx]
            if flag == False:
                val = -val
            take = val + solve(idx + 1, not flag)

            return max(take, skip)
        
        return solve(0, True)
    
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        '''
        Recursion + Memoization Solution:
        T.C: O(2N)
        '''
        n = len(nums)
        # t[n][2] [2] -> flag [n] -> index
        t = [[-1 for i in range(2)] for _ in range(n)]
        def solve(idx, flag):
            # If we have considered all elements
            if idx >= n:
                return 0
            if t[idx][flag] != -1:
                return t[idx][flag]
            skip = solve(idx + 1, flag)
            val = nums[idx]
            if flag == False:
                val = -val
            take = val + solve(idx + 1, not flag)

            t[idx][flag] = max(take, skip)
            return t[idx][flag]
        
        return solve(0, True)