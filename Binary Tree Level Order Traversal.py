# Leetcode Problem: 107. Binary Tree Level Order Traversal II
# Leetcode Link: https://leetcode.com/problems/binary-tree-level-order-traversal-
# Category: Tree, Breadth-First Search, Binary Tree
# Difficulty: Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        Explanation:
        To perform a level order traversal of a binary tree from bottom to top, we can use
        a queue to facilitate breadth-first search (BFS). We start by adding the root node
        to the queue. Then, we repeatedly process nodes level by level, adding their values to
        a temporary list for the current level. After processing all nodes at the current level,
        we append this list to the result. Finally, we reverse the result to get the bottom
        to top order.

        Time Complexity: O(n), where n is the number of nodes in the tree. Each node is processed once.
        Space Complexity: O(n), for storing the result and the queue in the worst case.

        '''
        q = deque()
        q.append(root)
        result = []

        if not root:
            return result 
        
        while q:
            level = []
            k = len(q)
            for _ in range(k):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                
                
            
            result.append(level)
        return result[::-1]