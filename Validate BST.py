# LeetCode 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/
# Difficulty: Medium

'''
Time Complexity: O(n) where n is the number of nodes in the tree. This is because we visit each node exactly once during the inorder traversal.
Space Complexity: O(n) in the worst case, which occurs when the tree is completely unbalanced (e.g., a linked list). In the average case, the space complexity is O(h), where h is the height of the tree, due to the recursion stack.

Explanation: 
The inorder traversal of a binary search tree (BST) produces a sorted sequence of values. Therefore, to validate whether a binary tree is a BST, we can perform an inorder traversal and check if the resulting sequence is strictly increasing.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = []
        # inorder = LPR 

        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)

        dfs(root)

        for i in range(len(inorder) - 1):
            if  inorder[i] >= inorder[i + 1]:
                return False
        return True         