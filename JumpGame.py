# Leetcode Link: https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150
# Category: Arrays, DP(optional)

# Approach 1: Smart way, linear time 
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # smart approach
        # basically from each start see which is the maxpoint you can reach 
        # if max point is >= goal then all good

        maxReach = 0
        n = len(nums)
        for i in range(n):
            if i > maxReach:  # If we reach an index we cannot get to, return False
                return False
            maxReach = max(maxReach, i + nums[i])

        if maxReach >= n - 1:
            return True 
        return False 

# Approach 2: Recursion 
# T.C: n elements and can jump k times for each O(n^k) exponential!
class Solution:
    def solve(self, nums, n, index):
        if index >= n - 1:
            return True 

        for i in range(1, nums[index] + 1):
            if self.solve(nums, n, index + i):
                return True
        return False

    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        return self.solve(nums, n, 0)

# Approach 3: Memoization 
# T.C: O(n)
class Solution:
    '''
    Basically see if from jumps you have reached the end 
    If not then take all the jumps from that point
    If any of the jumps resulted in reaching the end from that point we return true 
    '''
    def solve(self, nums, n, index, memSet):
        if index >= n - 1:
            return True 
        
        if memSet[index] != -1:
            return memSet[index]

        for i in range(1, nums[index] + 1):
            if self.solve(nums, n, index + i, memSet):
                memSet[index] = True
                return memSet[index]

        memSet[index] = False
        return memSet[index]

    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memSet = [-1] * n
        return self.solve(nums, n, 0, memSet)

        
