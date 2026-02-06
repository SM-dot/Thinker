# Leetcode: https://leetcode.com/problems/path-sum-ii/
# leetcode Problem: 113. Path Sum II
# Category: Tree, Depth-First Search, Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        '''
        Explanation:
        To find all root-to-leaf paths in a binary tree where the sum of the node
        values equals a given target sum, we can use a depth-first search (DFS) approach.

        Time Compelxity: O(n), where n is the number of nodes in the tree. In the worst case, we may have to visit all nodes to find all valid paths.
        Space Complexity: O(h), where h is the height of the tree. This space is used by the recursion stack and the path list. In the worst case (skewed tree),
        '''
        self.result = []

        def dfs(node, currSum, path):
            if not node:
                return 
            
            currSum += node.val
            path.append(node.val)
            if node.left == None and node.right == None:
                if currSum == targetSum: 
                    self.result.append(path[:])
            else:
                dfs(node.left, currSum, path)
                dfs(node.right, currSum, path)
            path.pop()
        
        dfs(root, 0, [])
        return self.result 