# Leetcode Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Problem Number: 104
# Category: Trees 

'''
Think of it simply. Lets say you are at the top of the tree, you want to find the longest path to the ground. Now you have branches/ nodes on the left and right
The longest path could either be the left one or the right one. 
So total number of branches/ nodes you are on will be the maximum of the nodes on the left or right + current top node you are standing on
Have faith that you will know which path is longer that is - left path or the right path 
In the case that you are on the ground, root = 0. There is no need to travel on any nodes, so your answer will be 0. 

Time Complexity: You will visit all the nodes in the tree thus O(n)
Space Complexity: Recursive calls - O(n)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
