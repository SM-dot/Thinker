# LeetCode Problem: Binary Tree Max Path Sum
# Problem Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Category: Tree, DFS
from collections import defaultdict

'''
Input: A binary tree represented by its root node
Operations:
- Use DFS to traverse the tree and calculate the maximum path sum
- For each node, calculate the maximum path sum that can be formed by including the node and its left and right children
Output: The maximum path sum in the binary tree
T.C: O(N) where N is the number of nodes in the tree
S.C: O(H) for the recursion stack, where H is the height of the tree
Using DFS to calculate the maximum path sum in the binary tree  
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float('-inf')

        def solve(rootNode):
            nonlocal result
            if not rootNode:
                return 0

            left = solve(rootNode.left)
            right = solve(rootNode.right)

            case1 = left + right + rootNode.val
            case2 = max(left, right) + rootNode.val
            case3 = rootNode.val
            
            result = max(result, case1, case2, case3)
            return max(case2, case3)
        
        solve(root)
        return result 