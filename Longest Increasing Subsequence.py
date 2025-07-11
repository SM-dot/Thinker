# LeetCode 300. Longest Increasing Subsequence
# Problem Link: https://leetcode.com/problems/longest-increasing-subsequence/
# Category: Dynamic Programming, Recursion, Memoization, Binary Search


# Recursive 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        To build the subsequence you can either take an element or skip it

        You can only take an element if it is greater than the last element in the sequence. 

        T.C: O(2^n) recursion
        T.C: O(n^2) memoization
        '''
        n = len(nums)
        dp = [[-1 for j in range(n + 1)] for i in range(n + 1)]
        def solve(idx, prevIndex):
            if idx >= n:
                return 0
            
            if dp[idx][prevIndex] != -1:
                return dp[idx][prevIndex]
            # take an element in the subsequence 
            take = 0
            if (prevIndex == -1 or nums[idx] > nums[prevIndex]):
                # 1 + cause increasing the lenght of the subsequence
                # updating prevIndex cause this new element got added
                take = 1 + solve(idx + 1, idx)
            
            # skip an element
            skip = solve(idx + 1, prevIndex)
            # cause the longest subsequence can be if we add that element or skip it - whichever is max 
            dp[idx][prevIndex] = max(take, skip)
            return dp[idx][prevIndex]
        
        return solve(0, -1)

# Recursive + Memoization 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        To build the subsequence you can either take an element or skip it

        You can only take an element if it is greater than the last element in the sequence. 

        T.C: O(2^n) recursion
        T.C: O(n^2) memoization
        '''
        n = len(nums)
        dp = [[-1 for j in range(n + 1)] for i in range(n + 1)]
        def solve(idx, prevIndex):
            if idx >= n:
                return 0
            
            if dp[idx][prevIndex] != -1:
                return dp[idx][prevIndex]
            # take an element in the subsequence 
            take = 0
            if (prevIndex == -1 or nums[idx] > nums[prevIndex]):
                # 1 + cause increasing the lenght of the subsequence
                # updating prevIndex cause this new element got added
                take = 1 + solve(idx + 1, idx)
            
            # skip an element
            skip = solve(idx + 1, prevIndex)
            # cause the longest subsequence can be if we add that element or skip it - whichever is max 
            dp[idx][prevIndex] = max(take, skip)
            return dp[idx][prevIndex]
        
        return solve(0, -1)
            
# Bottom Up DP
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        t = [1 for i in range(n)]
        # t[i] = LIS ending at index i or abhi tak ka LIS

        # cause longest LIS is atleast 1 {10}, {9} etc thats why keeping it 1, while empty set is possible obviously when u can have one element in it that would be the longest before we start computing
        maxLIS = 1
        for i in range(0, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    t[i] = max(t[i], t[j] + 1)
                    maxLIS = max(maxLIS, t[i])
                    
        return maxLIS