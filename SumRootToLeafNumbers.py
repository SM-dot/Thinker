# Leetcode Link: https://leetcode.com/problems/sum-root-to-leaf-numbers/?envType=study-plan-v2&envId=top-interview-150
# Category: Tree 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
This solution tackles the problem of finding the total sum of all numbers formed by root-to-leaf paths in a binary tree.

The key insight is that as we traverse the tree, we build a number by appending digits represented by each node's value.
For example, a path 1 -> 2 -> 3 forms the number 123.

To achieve this, we use a recursive depth-first search (DFS) approach.
At each node, we multiply the current number by 10 and add the node’s value to simulate digit placement.
When we reach a leaf node (a node with no children), we add the accumulated number to a running total.

We use a helper function `inorder` (although the name suggests in-order traversal, the strategy here is actually pre-order DFS)
which carries along the current number formed so far. A `nonlocal` variable `sum` is used to keep track of the final result
across recursive calls.

This approach ensures all root-to-leaf paths are considered and their corresponding numbers are summed efficiently.

Time Complexity (T.C.): O(N), where N is the number of nodes in the tree — we visit each node exactly once.
Space Complexity (S.C.): O(H), where H is the height of the tree — this is the maximum depth of the recursion stack. 
In the worst case (unbalanced tree), H can be N; in the best case (balanced tree), H is log(N).
"""

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sum = 0

        def inorder(root, number):
            nonlocal sum
            if not root:
                return 0

            element = root.val
            number = number * 10 + element 

            if root.left == None and root.right == None: 
                sum += number 
                return 
            
            inorder(root.left, number)
            inorder(root.right, number)
        inorder(root, 0)
        return sum
