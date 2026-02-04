# LeetCode Problem Link: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
# LeetCode Problem: 323. Number of Connected Components in an Undirected Graph
# Category: Depth-First Search, Breadth-First Search, Union Find, Graph
# Difficulty: Medium

# Time Complexity: O(E * α(N)), where E is the number of edges and α is the inverse Ackermann function, which grows very slowly. This is due to the union-find operations.
# Space Complexity: O(N) for storing the parent and rank arrays.

# can also be done using DFS or BFS
# then the time complexity will be O(N + E) and space complexity O(N)
# therefore the better approach is union find here

class DSU: 
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
    
    def find(self, x):
        if self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent == y_parent:
            return 
        
        if self.rank[x_parent] > self.rank[y_parent]:
            self.parents[y_parent] = x_parent
        elif self.rank[y_parent] > self.rank[x_parent]:
            self.parents[x_parent] = y_parent
        else:
            self.parents[x_parent] = y_parent
            self.rank[y_parent] += 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)


        for u, v in edges:
            dsu.union(u, v)

        parents = set()

        for i in range(n):
            parents.add(dsu.find(i))
        
        return len(parents)
        