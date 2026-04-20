# Leetcode 1855: Maximum Distance Between a Pair of Values
# Problem Link: https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/
# Category: Array, Two Pointers
# Difficulty: Medium


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        Basically two pointer approach for a linear solution. 

        Brute force would be to compare all i and j pairs, but we can do better. 

        Think like this, we have two contraints: 
        1. i <= j 
        2. nums1[i] <= nums2[j]

        you keep two pointers i and j, both start at 0. 
        then you keep on iretating till both are in the nounds, if any goes out of bounds u have to quit cause it is no longer valid. 
        This above thingie happens cause length of nums1 and nums23 is not guaranteed

        Next, you need to make sure that the value at nums[i] > nums[j]
        if not increase i 
        if it is less our second consition satisfies store that in the result and move the j pointer ahead, why do we move j ahead? 
        cause both the arrays are non increasing that means the values keep on decreasing, and u wanna maximize the distance which is given bu j - i. 

        Note even if nums at i is less that nums j and lets say i is greater than j the way we are claculating the distacne automatically the result wont be added cause it would be a negative value. 

        result = max(result, j - i) and if i >= j then 3 - 5 would be negative and not recorded in
        This gives us a linear time solution. 

        Now let's code!
        '''
        n = len(nums1)
        m = len(nums2)
        i = 0
        j = 0 

        result = 0 

        while i < n and j < m:
            if nums1[i] > nums2[j]:
                i += 1
            else: 
                result = max(result, j - i) # j - i cause that is how it is given that the result will be calcualted. 
                j += 1
        
        return result 