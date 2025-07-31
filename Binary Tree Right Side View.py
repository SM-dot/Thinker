# Leetcode 199. Binary Tree Right Side View
# Problem Link: https://leetcode.com/problems/binary-tree-right-side-view/
# Category: Tree, BFS


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Input: A binary tree represented by its root node
        Operations:
        - Use BFS to traverse the tree level by level
        - For each level, keep track of the last node visited, which will be the rightmost node at that level
        Output: A list of values representing the right side view of the binary tree
        T.C: O(N) where N is the number of nodes in the tree        
        S.C: O(N) for the queue used in BFS
        Using BFS to get the right side view of the binary tree'''
        q = deque()
        q.append(root)
        answer = []

        if not root:
            return answer
            
        while q:
            n = len(q)
            for _ in range(n):
                element = q.popleft()
                last = element.val

                if element.left:
                    q.append(element.left)

                if element.right:
                    q.append(element.right)
            answer.append(last)
        
        return answer 
