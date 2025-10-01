# Leetcode Problem: 1658. Minimum Operations to Reduce X to Zero
# Link: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
# Difficulty: Medium
# Category: Sliding Window, Two Pointers, Array



class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        '''
        Think of the question a little differently. 
        Basically in order for x to be 0 we need an equal amount to be removed from it. 
        [1, 1, 4, 2, 3] = 1 + 1 + 4 + 2 + 3 = 11
        x = 5
        we need to find the LONGEST subarray with sum 11 - 5 = 6
        this will tell us how many minimum number of operations to do. 
        So the problem boils down to finding the longest subarray with sum = target

        In this example [1, 1, 4, 2, 3]
        longest subarray with sum 6 is [1, 1, 4]
        which means the remaning numbers sum to x which is correct 2 + 3 = 5 
        Ahah! This is the answer. 
        Note if you took a greeddy approach here then you would be missing many cases, for example chosing between values that are both less than x but might serve better in the long run. 

        T.C: O(n)
        S.C: O(1) we are not taking any extra space! :)
        Now let's code 
        '''
        total = sum(nums)
        target = total - x
        n = len(nums)
        left = 0
        maxLength = -1
        currSum = 0

        # Edge basic cases:
        if x == 0:
            return n
        
        if x > total:
            return -1 

        for right in range(n):
            currSum += nums[right]

            while currSum > target and left <= right: 
                currSum -= nums[left]
                left += 1
            
            if currSum == target:
                maxLength = max(maxLength, right - left + 1)
        
        if maxLength == -1:
            return -1
        else:
            return n - maxLength
