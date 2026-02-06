# LeetCode Problem Link: https://leetcode.com/problems/path-sum/
# LeetCode Problem: 112. Path Sum
# Category: Tree, Depth-First Search, Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(n), where n is the number of nodes in the tree. In the worst case, we may have to visit all nodes to find a path that sums up to the target.
# Space Complexity: O(h), where h is the height of the tree. In the worst case (skewed tree), h can be equal to n (number of nodes), making the


# Explanantion: 
# To determine if there is a root-to-leaf path in a binary tree that sums up to a given target, we can use a depth-first search (DFS) approach. We will traverse the tree starting from the root and keep track of the cumulative sum of the node values along the path. When we reach a leaf node (a node with no left or right children), we will check if the cumulative sum equals the target sum. If it does, we return true. If we exhaust all paths without finding a match, we return false.
# Note we do not need to backtrack here as in python for currSum in each call it is treated as different in isolation. So it works, in path sum 3 it was gloabl that is wny we need to backtrack 

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, currSum):
            if not node:
                return False
            
            currSum += node.val
            if node.right == None and node.left == None: 
                return currSum == targetSum
            
            return dfs(node.right, currSum) or dfs(node.left, currSum)
        
        return dfs(root, 0)