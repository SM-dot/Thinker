# Leetcode Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/?envType=study-plan-v2&envId=top-interview-150
# Category: Trees

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # Initialize a queue for level-order traversal (BFS)
        q = deque()
        q.append(root)

        # Edge case: if the tree is empty, return None
        if not root:
            return 

        # Perform BFS level by level
        while q:
            n = len(q)  # Number of nodes in the current level
            level = []  # Temporary list to store nodes at this level
            
            # Process all nodes in the current level
            for i in range(n):
                node = q.popleft()  # Dequeue the next node
                level.append(node)  # Store it in the level list

                # Enqueue left child if it exists
                if node.left:
                    q.append(node.left)
                
                # Enqueue right child if it exists
                if node.right: 
                    q.append(node.right)

            # Set the `next` pointers for all nodes in this level
            for i in range(len(level)):
                if i == len(level) - 1:
                    level[i].next = None  # Last node in the level points to None
                else:
                    level[i].next = level[i+1]  # Point current node to the next node in the level

        return root  # Return the modified tree
