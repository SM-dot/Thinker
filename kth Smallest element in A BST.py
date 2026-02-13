# LeetCode Problem Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# LeetCode Problem: 230. Kth Smallest Element in a BST
# Category: Tree, Depth First Search, Binary Search Tree
# Difficulty: Medium


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time complexity: O(n) in the worst case when the tree is skewed, but on average it is O(log n) for a balanced BST. This is because we are doing an inorder traversal and we are visiting each node once.
# Space complexity: O(h) where h is the height of the tree, which is O

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        traversal = []
        self.count = k 

        def inorder(root):
            if not root:
                return 
            
            inorder(root.left)
            self.count -= 1
            if self.count == 0:
                self.result = root.val
                return 

            inorder(root.right)
        
        inorder(root)
        return self.result
