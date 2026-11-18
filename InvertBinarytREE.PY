# leetcode Problem: 226. Invert Binary Tree
# leetcode Link: https://leetcode.com/problems/invert-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left, root.right = right, left
        return root