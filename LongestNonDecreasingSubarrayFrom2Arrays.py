# LeetCode Problem Link: https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/
# LeetCode Problem: 2810. Longest Non-Decreasing Subarray From Two
# Category: Dynamic Programming, Recursion
# Difficulty: Medium

class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        Basically from each point in the array we want to know if we can form a longest subarray or not. 
        Thus we call our solve function from each point. 

        In the recurisve function, we keep track of the precious value. However, if u think a bit longterm u will realise that the previous value could hold any numbers from 1 <= nums1[i], nums2[i] <= 109 making our dp very large. Instead we just hold if we sleected nums1 or nums2 in the process. this keeps the DP array shorter. 

        in recursion for each cell u are basically asking if it is greater than the previous cell then yes include it, and check the max path u can get. Simialrly select from the second array as well. 
        The recursive function has a tc of 2^n and since u are calling for each index in each array 2n therefore the total becomes n * 2^n 

        when u memoize u get 2n(recurisioon dp array) * n = O(n)

        Seems challenging but break it down and use recurisve faith to solve  
        '''
        n = len(nums1)
        dp = [[-1 for _ in range(2)] for _ in range(n)]

        def longestArray(i, lastChoice):
            if i >= n:
                return 0 

            if dp[i][lastChoice] != -1:
                return dp[i][lastChoice]

            if lastChoice == 1:
                lastNumber = nums2[i - 1]
            else:
                lastNumber = nums1[i - 1]

            res = 0
            if nums1[i] >= lastNumber:
                res = max(res, 1 + longestArray(i + 1, 0))

            if nums2[i] >= lastNumber:
                res = max(res, 1 + longestArray(i + 1, 1))
            
            dp[i][lastChoice] = res
            return dp[i][lastChoice]
        
        answer = 0
        for i in range(n):
            answer = max(answer, 1 + longestArray(i + 1, 0))
            answer = max(answer, 1 + longestArray(i + 1, 1))
        return answer 

