# LeetCode 993. Cousins in Binary Tree
# Problem Link: https://leetcode.com/problems/cousins-in-binary-tree/
# Category: Tree, BFS, DFS


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        '''
        Input: Root of binary tree, two values x and y
        Operations:
        - Use BFS to traverse the tree level by level
        - Track the parent and depth of each node
        - Check if x and y are at the same depth but have different parents
        Output: True if x and y are cousins, False otherwise
        T.C: O(N) where N is the number of nodes in the tree    
        S.C: O(N) for the queue and nodeInfo dictionary
        '''
        nodeInfo = defaultdict(list)
        q = deque()
        q.append(root)
        #            parent, level
        nodeInfo[root] = [-1, 0]
        level = 0

        while q:
            level += 1
            n = len(q)
            for _ in range(n):
                element = q.popleft()

                if element.left:
                    q.append(element.left)
                    nodeInfo[element.left.val] = [element.val, level]
                
                if element.right:
                    q.append(element.right)
                    nodeInfo[element.right.val] = [element.val, level]
        
        if nodeInfo[x] and nodeInfo[y] and nodeInfo[x][1] == nodeInfo[y][1] and nodeInfo[x][0] != nodeInfo[y][0]:
            return True
        return False 



# Another approach: 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:
        '''
        2 criterias for cousin:
        1. both are on the same level 
        2. both of them have different parents, if same parents then they are siblings!!!! 
        hehehehe, so not that straightforward ened to keep track of the parent as well. 
        Can probably do a dfs and find the x, y node and the parent as well. 
        or do bfs and keep track od the node information. 

        Now let's code 
        '''
        q = deque()
        q.append([root, -1])
        foundX = False 
        foundY = False 


        while q:
            k = len(q)
            for i in range(k):
                node, parent = q.popleft()

                if node.val == x:
                    xParent = parent
                    foundX = True 
                
                if node.val == y:
                    yParent = parent 
                    foundY = True 
                
                if node.left:
                    q.append([node.left, node])
                
                if node.right: 
                    q.append([node.right, node])

            if foundX and foundY:
                return yParent != xParent
            if foundX or foundY:
                return False 
                    