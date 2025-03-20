# Leetcode Problem number: 261
# Free version on Neetcode.io
# Category: Trees and Graphs 


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # the main thing is that there should not be a cycle, if there 
        # is a cycle means that we can classify it as a graph
        # if multiple components or 2 trees, still incorrect as we are only checking for 1 tree
        # Will have n nodes, start a traversal from the 0th node
        # If you find no cycle and visited nodes == n => all good it is a tree
        # If you fing no cycle and visited nodes != n => 2 or more components/ trees therefor return false

        # if no nodes in a tree, it can still be considered a tree
        if not n:
            return True
        visit = set()
        # hashmap
        adj = [[] for i in range(n)]
        # populating the hashmap
        for edge in edges:
            a = edge[0]
            b = edge[1]
            adj[a].append(b)
            adj[b].append(a)

        # cycle detection 
        def cycle_detection(node, parent):
            visit.add(node)
            for ngbr in adj[node]: 
                if ngbr == parent:
                    continue
                if ngbr in visit:
                    return True
                if cycle_detection(ngbr, node):
                    return True
            return False 
        
        return not cycle_detection(0, -1) and len(visit) == n

