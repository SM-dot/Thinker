# Leetcode: https://leetcode.com/problems/jump-game/
# Category: Array, Greedy
# Difficulty: Medium


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        Brute force would be to take each jump and then see where I can go from there. If I keep on jumping max, can I do greedy here, Porbably not what if a smaller jump gives a better answer. Instead think like this: 
        go ahead and visit the nodes, once at that node go from there, for each node store if can reach tht ened or not. Porbably a dp question here. 

        However, a greedy appraoch here has a cleaner solution and works better. The main idea is to iterate from the back and make the intial goal the last index position, as u move back if there is a way to reach the goal from i, you now change the goal to i. cause u kno from i, i can reach the goal, so now I need to find if there is a way to reach the new goal which is i instead. 

        Greedy sinmple solution works in O(n) and actually does not need a recurisve approach cause then u would have a recursive overhead. 

        
        Time complexity: O(n) where n is the number of elements in the input array. This is because we are iterating through the array once from the end to the beginning, checking if we can reach the current goal from each index.
        Space complexity: O(1) as we are using a constant amount of extra space to
        store the goal index and a few variables for iteration, regardless of the input size.

        
        Ok, now let's code! 
        '''

        n = len(nums)
        goal = n - 1

        for i in range(n - 1, -1, -1):
            if i + nums[i] >= goal: 
                goal = i 
            
            if goal == 0: 
                return True 
        
        return False 
