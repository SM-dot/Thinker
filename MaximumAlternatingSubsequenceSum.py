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
        S.C: O(N) - recursion stack + O(N) - memoization array
        2N cause for each index we have 2 states - take or skip
        2 states - take or skip
        1 state - index
        Total states = 2N
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
    

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        '''
        Brute force: 
        find all subsequences(2^n time), for each subsequence find the alternating sum (n time)
        T.C: O(2^N * N)

        Bottom Up approach
        T.C: O(2N)
        '''
        n = len(nums)
        # t[n][2] [2] -> flag [n] -> index
        # indexing 1...n
        # t[i][even/odd] = whats the result when we take or skip the ith element such that forming an even/odd length subsequence 
        t = [[0 for i in range(2)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            # If taking/skipping the element at the ith index forms a subsequence of even length:     
            #            taking element          skipping element
            t[i][0] = max(t[i-1][1] - nums[i-1], t[i-1][0]) 


            # If taking/skipping the element at the ith index forms a subsequence of odd length 
            t[i][1] = max(t[i-1][0] + nums[i-1], t[i-1][1])
        
        # even length subsequence or odd length subsequence gives the answer 
        return max(t[n][1], t[n][0])
       
# RV Aug 3, 2025
# RV AUG 11, 2025
# RV AUG 31, 2025
# RV FEB 23, 2026 
