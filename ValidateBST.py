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

# This does an inorder traversal but does not take any extra space cause we keep track of the previous value seen in the inorder traversal, if we see a value that is less than or equal to the previous value then we know it is not a BST.
# it is crucial to keep self.prev as a global variable because we need to keep track of the previous value across all recursive calls, if we use a local variable it would not work as it would be reset in each recursive call.
# cause note if just get the prev of the root, it is possible that that small tree is a BST but the right subtree of the root has a value that is less than the root, thus we need to keep track of the prev value across all recursive calls.

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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # if a BST is a BST then an inorder traversal of a BST would give us a sorted array. 

        self.prev = float('-inf')
        def inorder(root):
            if not root: 
                return True 
            
            if not inorder(root.left):
                return False 
            
            if root.val <= self.prev:
                return False 
            self.prev = root.val

            return inorder(root.right)
        
        return inorder(root)
        

            
            

'''
# EXPLANATION:
The "Chain of Trust"

For any given node to be part of a valid BST, three specific conditions must be true:

Faith in the Left: The entire left subtree must be a valid BST.

The Current Node: The current node must be greater than the last value we saw (self.prev).

Faith in the Right: The entire right subtree must be a valid BST.

The Breakdown of the Code

Python
def inorder(node):
    if not node: 
        return True # Base Case: An empty tree is technically a valid BST.

    # 1. TEST THE LEFT: "I have faith that this call will tell me if 
    # the entire left side is valid."
    if not inorder(node.left):
        return False # If my faith was met with a 'False', the whole tree is ruined.

    # 2. TEST THE CURRENT: This is the only part I am manually checking.
    if node.val <= self.prev:
        return False
    self.prev = node.val # Update the 'global' last-seen value.

    # 3. TEST THE RIGHT: "I have faith that the right side knows 
    # if it's valid or not."
    return inorder(node.right) 
Why we MUST return the Right Call

If you just wrote inorder(node.right) without the return, you are basically saying:

"Hey Right Subtree, go check yourself... but I don't actually care what you find out. I'm not going to report your answer back to my boss."

Because the Right Subtree is the last thing that happens in an In-order traversal, its result is the "final verdict" for that entire branch of the tree.

If the right subtree is valid, it returns True.

If it's invalid, it returns False.

By saying return inorder(node.right), you are passing that final verdict up the chain to the parent node.

The "Leap of Faith" Summary

If the Left is valid (True) AND the Current node is valid, then the validity of the entire current tree depends entirely on whether the Right subtree is valid.
'''