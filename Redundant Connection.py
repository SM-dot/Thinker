# Leetcode Problem 684: Redundant Connection
# Link: https://leetcode.com/problems/redundant-connection/
# Difficulty: Medium

'''
Explanation:
Given a graph that started as a tree with n nodes (labeled from 1 to n
), with one additional edge added. The added edge connects two different vertices and was not an edge that already existed in the tree. The task is to find the edge that, when removed, will leave the graph as a tree of n nodes.
We can use the Disjoint Set Union (DSU) or Union-Find data structure to efficiently detect the cycle created by the added edge. The idea is to iterate through each edge and use the union operation to connect the nodes. If we find that two nodes are already connected (i.e., they have the same root), then the current edge is the redundant connection.
Time Complexity: O(n α(n)) where n is the number of edges and α is the Inverse Ackermann function, which grows very slowly. In practice, this is almost constant time.
Space Complexity: O(n) for storing the parent and size arrays in the DSU.

'''
class DSU: 
    def __init__(self, n):
        self.parents = [i for i in range(n + 1)]
        self.size = [1 for i in range(n + 1)]
    
    def find(self, x):
        if self.parents[x]==x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent == y_parent:
            return 
        
        if self.size[x_parent] > self.size[y_parent]:
            self.size[x_parent] += self.size[y_parent]
            self.parents[y_parent] = x_parent
        else:
            self.size[y_parent] += self.size[x_parent]
            self.parents[x_parent] = y_parent


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n)

        for u, v in edges: 
            if dsu.find(u) == dsu.find(v):
                return [u, v]
            dsu.union(u, v)


        