# lEETCODE PROBLEM: 144. Binary Tree Preorder Traversal
# Leetcode Link: https://leetcode.com/problems/binary-tree-preorder-traversal/
# Category: Tree, Depth-First Search, Binary Tree
# Difficulty: Easy



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Expalanation:
    To perform a preorder traversal of a binary tree, we can use a depth-first search (
    DFS) approach. In preorder traversal, we visit the root node first, followed by the left
    subtree, and finally the right subtree. We can implement this using a recursive function
    that appends the value of each visited node to a result list.
    Time Complexity: O(n), where n is the number of nodes in the tree. Each node is visited once.
    Space Complexity: O(h), where h is the height of the tree. This space is used by the recursion stack.
    '''
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
    
        def dfs(root):
            if not root: 
                return None
            
            result.append(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return result 