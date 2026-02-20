# LeetCode Problem Link: https://leetcode.com/problems/evaluate-boolean-binary-tree/
# LeetCode Problem: 2331. Evaluate Boolean Binary Tree
# Category: Tree, Depth-First Search, Binary Tree
# Difficulty: Easy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # use recursion 
        # traverse the tree 
        # get the left value and right value accordingly put in the formula and solve 

        def solve(root):
            if not root.left and not root.right: 
                return root.val
            
            left = solve(root.left)
            right = solve(root.right)

            if root.val == 2:
                return left or right
            
            if root.val == 3:
                return left and right 
        
        
        answer = solve(root)
        if answer == 1:
            return True 
        if answer == 0:
            return False 