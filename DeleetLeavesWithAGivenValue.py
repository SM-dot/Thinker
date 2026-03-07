# Leetcode Problem Link: https://leetcode.com/problems/delete-leaves-with-a-given-value/
# LeetCode Problem: 1325. Delete Leaves With a Given Value
# Category: Tree, Depth-First Search
# Difficulty: Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        '''
        USe recursive faith here, assume that ur left and right trees are solved and returned to u. Then the only thing u are thibnking about is that if my cirrent leaf also has the node value as the targte then what happens. 

        The problem becomes a lot simpler and fun that way, the time complexity remain O(n) since u visit all the nodes once in the tree, space complexity would be the same as the recursive stack. 
       
        Time complexity: O(n) where n is the number of nodes in the binary tree. This is because we are visiting each node exactly once to check if it is a leaf node with the target value and to potentially delete it.
        Space complexity: O(h) where h is the height of the binary tree, due to
        
       '''

        def deleteNode(root):
            if not root: 
                return None 
            
            leftVal = deleteNode(root.left)
            root.left = leftVal
            rightVal = deleteNode(root.right)
            root.right = rightVal 

            if not leftVal and not rightVal and root.val == target:
                return None
            
            return root
        
        return deleteNode(root)