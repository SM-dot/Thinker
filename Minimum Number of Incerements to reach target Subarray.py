# LeetCode Problem 1824: Minimum Number of Increments to Reach Target Subarray
# LeetCode Link: https://leetcode.com/problems/minimum-number-of-increments-to-re
# Category: Array, Greedy
# Difficulty: Medium

# Explanation:
# To determine the minimum number of increments needed to reach the target array from an initial array of   
# zeros, we can iterate through the target array while keeping track of the previous value. For each element in
# the target array, if the current value is greater than the previous value, we need to
# increment the count by the difference between the current and previous values. This is because
# we can achieve the current value by incrementing from the previous value. If the current
# value is less than or equal to the previous value, no additional increments are needed since
# we can achieve it through previous increments. By summing up all the required increments,
# we can obtain the minimum number of increments needed to reach the target array.  
# Time Complexity: O(n), where n is the length of the target array, as we need to iterate through the array once.
# Space Complexity: O(1), as we are using a constant amount of extra space.

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # [0,0,0,0,0]
        # [1,2,3,2,1]
        # prev = 0(base condition to start with)  curr = 1
        # if prev < curr:
        # incrment += 1
        # prev = 1, curr = 2 
        # if prev < curr
        # increment += curr - prev
        # ..
        # now see the case when prev = 3 and curr 2 
        # the initial 
        # [1 1 1 1 1]
        # [1 2 2 2 1]
        # [1 2 3 2 1]
        # one of the initial increments would have incrmeented this curr already so we do not need to add it in. 
        # therefore these are the conditions 
        # if even decrements were allowed then you would have to use absolute while comparing the prev and curr, you would be doing this on the differnece array of initial and target. 
        # see leetcode 3229 for more clarity 

        prev = 0
        n = len(target)
        increments = 0


        for i in range(n):
            curr = target[i]
            if prev < curr:
                increments += curr - prev
            prev = curr # Do not forget this!!! 
        
        return increments