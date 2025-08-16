# # LeetCode 947. Most Stones Removed with Same Row or Column
# # Problem Link: https://leetcode.com/problems/most-stones-removed-with-same   
# # Category: Graph, Union Find (Disjoint Set Union)
"""
This solution uses Disjoint Set Union (DSU) to group stones connected by the same row or column.
Two stones are considered connected if they share a row or column. The goal is to remove as many stones 
as possible while ensuring at least one stone remains per connected group.

We union all stones that are in the same row or column. The number of moves possible is:
    total stones - number of connected groups

Time Complexity:
- O(n^2 * α(n)) where n is the number of stones, due to checking each stone pair and DSU operations.
  (α is the inverse Ackermann function, very slow-growing, so nearly constant in practice.)

Space Complexity:
- O(n) for storing parent and size arrays in the DSU.
"""

class DSU: 
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1 for i in range(n)]
    
    def find(self, x):
        if self.parents[x] == x:
            return self.parents[x]
        
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)
        if x_parent == y_parent:
            return 
        
        if self.size[x_parent] >= self.size[y_parent]:
            self.size[x_parent] += self.size[y_parent]
            self.parents[y_parent] = x_parent
        else:
            self.size[y_parent] += self.size[x_parent]
            self.parents[x_parent] = y_parent

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        dsu = DSU(n + 1)

        for i in range(n):
            for j in range(i, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    dsu.union(i, j)
        
        # number of groups:
        groups = set()
        for i in range(n):
            groups.add(dsu.find(i))
        
        return n - len(groups)
