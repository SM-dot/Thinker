# Leetcode Link: https://leetcode.com/problems/subtree-of-another-tree/
# Problem Number: 572
# Category: Trees 

# Approach:
# The problem requires checking if `subRoot` is a subtree of `root`.
# Instead of searching blindly, we break the problem into two parts:
#   1. Checking if two trees are identical (`isSame` function).
#   2. Recursively traversing `root` to find a potential match (`isSubtree` function).
# 
# - The `isSame` function determines if two trees are structurally identical with the same values.
#   - If both nodes are None, they are trivially identical.
#   - If one node is None while the other is not, they cannot be the same.
#   - If both nodes exist and have the same value, check their left and right children recursively.
#   - The key insight is that for `subRoot` to be a subtree, it must be an exact match with some subtree of `root`.
# 
# - The `isSubtree` function explores `root` to find a subtree that matches `subRoot`:
#   - If `subRoot` is None, it is always a valid subtree (trivial case, return True).
#   - If `root` is None but `subRoot` is not, then `subRoot` cannot exist in `root` (return False).
#   - If `root` and `subRoot` have the same value, we check if they are identical using `isSame`.
#   - Otherwise, `subRoot` might still be present in either the left or right subtree of `root`, so we continue searching.
#   - The key insight is that at every step, we either find an exact match or continue exploring deeper.
# 
# Time Complexity:
# - `isSame` runs in O(N), where N is the number of nodes in `subRoot`, since we check every node in the subtree.
# - `isSubtree` checks every node in `root`, leading to O(M) calls where M is the number of nodes in `root`.
# - In the worst case, each node in `root` is checked against `subRoot`, leading to an overall O(M * N) complexity.
#   - This worst case happens when all nodes in `root` have the same values as `subRoot` but different structures.
# 
# Space Complexity:
# - The recursion depth in the worst case is O(M) for `isSubtree` and O(N) for `isSame`.
# - Thus, the total worst-case auxiliary space is O(M + N), primarily due to recursion stack space.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSame(self, a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val == b.val:
            return self.isSame(a.left, b.left) and self.isSame(a.right, b.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if root.val == subRoot.val and self.isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
