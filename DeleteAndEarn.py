# LeetCode Problem Link: https://leetcode.com/problems/delete-and-earn/
# LeetCode Problem: 740. Delete and Earn
# Category: Dynamic Programming, Array
# Difficulty: Medium


class Solution:
    '''
    Explnantion
    First count the number of duplicates cause whatever u are doing for a single 4 can also be done for all other 4's so keep count of that
    Next, remove the duplicates and sort the array
    essentially the problem boils down to a house robber problem 
    include exclude principle 
    the include has a caviat that if the next number is +1 difference then u cannot include it, if not then include it. And then see what happens by removing it
    This solution is built off from the recursion solution and then a dp table is added to it to optimize it.
    Recursion solution TC: O(2^n) where n is the number of unique elements in the array, as each element can either be included or excluded.
    DP solution TC: O(n) where n is the number of unique elements in the array
    SC: O(n) for the dp table and the recursion stack in the worst case, where n is the number of unique elements in the array.
    Can be optimized further more if we ignore the table and keep track of 2 variables 
    '''
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        nums = list(set(nums))
        nums.sort()
        n = len(nums)
        dp = [-1] * (n + 1)

        def earn(numIndex):
            if numIndex >= n:
                return 0 
            
            if dp[numIndex] != -1:
                return dp[numIndex]

            currPoints = count[nums[numIndex]] * nums[numIndex]

            if numIndex + 1 < n and nums[numIndex] == nums[numIndex + 1] - 1:
                # this means that we cannot include the next number 
                includeNum = currPoints + earn(numIndex + 2)
            else:
                # this means that there were no conflicts 
                includeNum = currPoints + earn(numIndex + 1)
            
            excludeNum = earn(numIndex + 1)
            dp[numIndex] = max(includeNum, excludeNum)
            return dp[numIndex]
        
        return earn(0)






# Bottom Up Approach 
from collections import defaultdict 
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for num in nums: 
            count[num] += 1
        
        nums.sort()
        nums = list(set(nums))
        n = len(nums)
        dp = [0 for _ in range(n + 1)]

        dp[0] = nums[0] * count[nums[0]]

        for i in range(1, n):
            currPoints = nums[i] * count[nums[i]]
            includeNum = 0
            excludeNum = 0

            if nums[i] == nums[i - 1] + 1:
                if i - 2 >= 0:
                    includeNum = currPoints + dp[i - 2]
                else: 
                    includeNum = currPoints
            else: 
                includeNum = currPoints + dp[i - 1]
            
            excludeNum = dp[i - 1]
            dp[i] = max(includeNum, excludeNum)
        
        return dp[n -1]

