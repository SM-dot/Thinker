# Leetcode Link: https://leetcode.com/problems/validate-binary-search-tree/description/?envType=study-plan-v2&envId=top-interview-150
# Category: Trees 


# METHOD 1: 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        This solution will not take any extra space, recursive space - yes but no extra space. 

        Basically think of a simple tree, 1, 2, 3in the example 1 < 2 < 3
        This means we are setting up some sort of bounds to identify if it can be a BST or not. If you try a few more examples you will notice a pattern. 

        but first, let's set up the recursice faith: 
        we are going to create a recurisve function, let's call it validate. 
        Validate will tell us if that tree is a blaid BST or not

        Now, the pattern:
        for a tree to be BST the left and right tree also need to be a BST
        and all the values in the left tree need to be less than the current root 
        and all the values in the right tree need to be greater than the current root

        Simple! Now we have the boundaries, let's code :)
        '''

        def validate(root, left_boundary, right_boundary):
            if not root:
                return True 
            
            if not (left_boundary < root.val < right_boundary):
                return False
            
            left = validate(root.left, left_boundary, root.val)
            right = validate(root.right, root.val, right_boundary)
            return left and right 
        
        return validate(root, float(-inf), float('inf'))

  # METHOD 2
  '''
  We know that the inorder traversal of a BST gives us a sorted order. So we simply get the inorder traversal and see if it is sorted with a strictly increasing value
  '''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        order = []

        def inorder(root):
            nonlocal order
            if not root:
                return 

            inorder(root.left)
            order.append(root.val)
            inorder(root.right)
        
        inorder(root)

        for i in range(1, len(order)):
            if not order[i - 1] < order[i]:
                return False
        return True
