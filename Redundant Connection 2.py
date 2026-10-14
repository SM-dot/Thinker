# Leetcode: Redundant Connection II
# Problem Link: https://leetcode.com/problems/redundant-connection-ii/
# Category: Graph, DFS, BFS, Tree, Binary Tree, Union Find, Disjoint

class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n + 1)]
        self.size = [1 for i in range(n + 1)]
    
    def find(self, x):
        if x == self.parents[x]:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent == y_parent: 
            return False 
        
        if self.size[y_parent] < self.size[x_parent]:
            self.parents[y_parent] = x_parent
            self.size[x_parent] += self.size[y_parent]
        else:
            self.parents[x_parent] = y_parent
            self.size[y_parent] += self.size[x_parent]
        
        return True 

class Solution:
    def findRedundantDirectedConnection(self, edges: list[list[int]]) -> list[int]:
        '''
        For this question, think like this, when can we have a redundant edge: 
        1. When a node has more than one parent, then we have a few candidates and we make sure we consider them. Let's say we have candidate 1 and candidate 2, We then remove the candidate 1 and do a DSU and make sure that there are no cycles, if a cycle still exists we simpy return the other candidate
        2. We can have a redundant edge when we have a cycle, so again we do a cycle edge 

        I think this should cover it and give us the result. Let us code it up and see if we are missing any edge cases or not. 

        Now, let's code! 
        '''
        n = len(edges)
        parent_map = {}
        cand1 = cand2 = None

        # Step 1: Detect if any node has two parents
        for u, v in edges:
            if v in parent_map:
                cand1 = [parent_map[v], v]  # earlier edge
                cand2 = [u, v]              # later edge
                break
            parent_map[v] = u

        # Helper to check if edges form a cycle (optionally skipping one edge)
        def has_cycle(skip_edge: list[int] | None = None) -> list[int] | None:
            dsu = DSU(n)
            for u, v in edges:
                if skip_edge and [u, v] == skip_edge:
                    continue
                if not dsu.union(u, v):
                    return [u, v]  # Edge causing the cycle
            return None

        # Step 2: Handle cases based on in-degree conflict
        if cand1:
            # If skipping the second candidate still leaves a cycle, cand1 is the culprit
            if has_cycle(skip_edge=cand2):
                return cand1
            return cand2

        # Step 3: Pure cycle case (no node with two parents)
        return has_cycle()