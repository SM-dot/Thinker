# LeetCode Problem: 310. Minimum Height Trees
# Problem Link: https://leetcode.com/problems/minimum-height-trees/
# Category: Graph, Tree, BFS    

from collections import defaultdict, deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        Optimized: Find the centroids by trimming leaves (nodes with degree 1) until 1 or 2 nodes remain.
        T.C: O(n)
        S.C: O(n) for adjacency list and queue
        '''
        # Handle edge cases
        if n <= 2:
            return list(range(n))
        
        # Build adjacency list and degrees
        adj = defaultdict(set)
        degrees = [0] * n
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
            degrees[a] += 1
            degrees[b] += 1
        
        # Initialize queue with leaves (degree 1)
        trimLeaves = deque([leaf for leaf in range(n) if degrees[leaf] == 1])
        remainingLeaves = n

        # Trim leaves until 1 or 2 nodes remain
        while remainingLeaves > 2:
            size = len(trimLeaves)
            remainingLeaves -= size
            for _ in range(size):
                element = trimLeaves.popleft()
                for ngbr in adj[element]:
                    degrees[ngbr] -= 1
                    adj[ngbr].remove(element)  # Remove edge from neighbor
                    if degrees[ngbr] == 1:
                        trimLeaves.append(ngbr)
                adj.pop(element)  # Remove leaf from graph
        
        return list(trimLeaves)