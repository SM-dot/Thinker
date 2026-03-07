# LeetCode Problem Link: https://leetcode.com/problems/construct-quad-tree/
# LeetCode Problem: 427. Construct Quad Tree
# LeetCode Problem: 427. Construct Quad Tree
# Category: Tree, Divide and Conquer, Recursion
# Difficulty: Medium

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        '''
        Understand what the question is asking.
        Simple do what it is telling. 

        Key for me: 
        if the entire gird has the same value then it is a leaf, if it does not then it is not a leaf and u need to break it down further. 

        Look at the way it is cut. 

        Each time ur grid is getting smaller, so ur contraint changes to n/2 use that.

        The main recurisve loop runs log(n) times but the check to see if all the values are the same or not is actually n square. Cause u go thorugh each of the values and retunr the verdict

        Space Compelxity: log(n) recursive stack takes that much, as we keep on reducing the height by n/2 
        '''

        n = len(grid)

        def allSame(x, y, n):
            val = grid[x][y]

            for i in range(x, x + n):
                for j in range(y, y + n):
                    if grid[i][j] != val: 
                        return False
            return True 
    

        def solve(x, y, n):
            if allSame(x, y, n):
                return Node(grid[x][y], True)
            
            else: 
                root = Node("#", False)

                root.topLeft = solve(x, y, n//2)
                root.topRight = solve(x, y + n//2, n//2)
                root.bottomLeft = solve(x + n//2, y, n//2)
                root.bottomRight = solve(x + n//2, y + n//2, n//2)

                return root
        
        return solve(0, 0, n)

                

        