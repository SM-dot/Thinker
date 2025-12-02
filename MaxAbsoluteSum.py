# Leetcode Problem: 1749. Maximum Absolute Sum of Any Subarray
# Leetcode link: https://leetcode.com/problems/maximum-absolute-sum-of-any-sub
# Leetcode Problem Name: Maximum Absolute Sum of Any Subarray


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        '''
        Kadane's Algorithm:
        FINDS THE MAX SUBARRAY SUM 
        currSum = max(currSum + nums[i], nums[i])
        basically the running sum we have so far versus starting a new subarray
        maxSum = max(maxSum, currSum)
        

        For this question:
        we want to find the maximum subarray sum and minimum subarray sum and then chose the max of those as we are finding the absolute sum of the array. 

        T.C: O(N + N) = O(2N) = O(N)
        S.C: O(1)
        '''

        n = len(nums)

        def maxSubArraySum():
            currSum = nums[0]
            maxSum = nums[0]

            for i in range(1, n):
                currSum = max(nums[i], currSum + nums[i])
                maxSum = max(maxSum, currSum)
            return maxSum
        
        def minSubArraySum():
            currSum = nums[0]
            minSum = nums[0]

            for i in range(1, n):
                currSum = min(nums[i], currSum + nums[i])
                minSum = min(minSum, currSum)
            return minSum 
        
        a = minSubArraySum()
        b = maxSubArraySum()
        return max(abs(a), b)