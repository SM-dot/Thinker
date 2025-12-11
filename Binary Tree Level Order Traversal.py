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
        return result[::-1] # reversing the result to get bottom to top order, time complexity O(n)
    

# More explanation code, revised on December 10, 2025
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        super straightforward implementation of a breadtn first traversal here. 
        Basically, replace the nextnode with just chekcing the left and right nodes and we do not need to keep a visited array cause it is a tree and only works in one direction. For optimization instead of storing the full level of each level of the tree we are just appending the last value to the tree. This helps ion saving the memory storagr that we have. 
        Time Complexity: O(V + E) (simple TC of BFS)
        Space Complexity: O(N) (just the storage amount of the q and the answer) Since we optimised by not storing the entire level this is the best we can do here. 
        '''
        q = deque()
        q.append(root)

        if not root:
            return []

        answer = []
        while q:
            k = len(q)
            for i in range(k):
                node = q.popleft()
                if i == k - 1:
                    answer.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return answer 
