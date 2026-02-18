# LeetCode Problem Link: https://leetcode.com/problems/minimum-sum-of-two-arrays/
# LeetCode Problem: 2578. Minimum Sum of Two Arrays
# Category: Array, Greedy


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        Need to know 2 facts: 
        1. Cannot decrease a sum 
        2. Cannot modify a sum if zeroes 

        Key: since we want minimum , use a greedy approach. For every 0 replace with a 1. 
        If sum1 < sum2 
        we can increase sum1 to sum2 if sum1 had zeroes otherwise return -1

        vice versa. 

        O(n) TC: we need to iterate through both arrays once to get the sum and count of zeroes.
        O(1) SC: we are using a constant amount of extra space to store the sums and counts of zeroes for both arrays.
        '''

        sum1 = 0
        zeroes1 = 0

        sum2 = 0
        zeroes2 = 0

        for num in nums1:
            if num == 0:
                sum1 += 1
                zeroes1 += 1
            else:
                sum1 += num
        
        for num in nums2: 
            if num == 0:
                sum2 += 1
                zeroes2 += 1
            else:
                sum2 += num
        
        if sum1 < sum2 and zeroes1 == 0:
            return -1 
        
        if sum2 < sum1 and zeroes2 == 0:
            return -1 
        
        return max(sum1, sum2)
