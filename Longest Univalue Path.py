# Leetcode Problem: 687. Longest Univalue Path
# Leetcode Link: https://leetcode.com/problems/longest-univalue-path/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode | None) -> int:
        '''
        Main thing here is that we are not returning the number of nodes but the number of edges. So the answer for a leaf node is acrtully 0.

        Visually understanding the solution is easy, but while coding have to be careful of a few things. 

        What are we returning? 
        [The value of that subtree, the longest path in that subtree with that value]

        classic dfs solution. 

        time complexity: O(n) where n is the number of nodes in the tree. This is because we are traversing all the nodes in the tree once.
        space complexity: O(h) where h is the height of the tree. This is because
        '''
        self.result = 0

        def solve(root):
            # if no node
            if not root:
                return [float('-inf'), 0]
            
            # we have reached a leaf node 
            if not root.left and not root.right: 
                return [root.val, 0]
            
            # if we have some middle node
            left_val, left_longest = solve(root.left)
            right_val, right_longest = solve(root.right)
            
            if left_val == right_val == root.val: 
                self.result = max(self.result, 2 + left_longest + right_longest)
                return [root.val, 1 + max(left_longest, right_longest)]
            
            elif left_val == root.val: 
                self.result = max(self.result, 1 + left_longest)
                return [root.val, 1 + left_longest]
            
            elif right_val == root.val:
                self.result = max(self.result, 1 + right_longest)
                return [root.val, 1 + right_longest]
            
            # if none of the values match from the left or right side
            return [root.val, 0] #no path found yet
        
        solve(root)
        return self.result 