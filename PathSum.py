# LeetCode Problem Link: https://leetcode.com/problems/path-sum-iii/
# LeetCode Problem: 437. Path Sum III
# Category: Tree, Depth-First Search, Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        '''
        For this question, think of getting the path sum till a certain node, so for root node 10 what is the path sum so far 10, for 10->5 the sume is 15. 10->5->3 = 18. Let's say the target is 15 then we know currSum - target => 18 - 15 = 3, no we cannot get a path. For 10->5 cursum - tagte => 15 - 15 = 0. Yes u can always make zero by not taking anything in the tree. 

        Therefore use kinda two sum methodology. Keep track of the path sum and and build from there. Why not get the sum of the path from the left and then from the right becuase that doesnt work we need to build it in real time. 

        Also remeber when adding to the dictionary do not forget to remove that from the dictionary once u are done exploring it u cannot really go down or to the left. You are done with that node, that currSum does not exist cause u are moving back up.

        T.C: O(N)
        S.C: O(N)

        Now let's code!!! 
        '''
        self.paths = 0
        self.pathSums = defaultdict(int)
        self.pathSums[0] = 1 # there is 1 way to make a sum of 0 by not slecting any node 

        def dfs(node, currSum):
            if not node:
                return
            
            currSum += node.val
            self.paths += self.pathSums[currSum - targetSum]
            self.pathSums[currSum] += 1
            if node.right:
                dfs(node.right, currSum)
            if node.left:
                dfs(node.left, currSum)
            self.pathSums[currSum] -= 1 # you are now goign back up so this down path sum cannot be used, thus u remove it 
    
        dfs(root, 0)
        return self.paths 
            