# Leettcode Name: Add Edges to Make Degrees of All Nodes Even
# Leetcode Link: https://leetcode.com/problems/add-edges-to-make-degrees-of
# All-Nodes-Even/
# Category: Graph, DFS, BFS, Tree, Binary Tree, Union Find, Disjoint


class Solution:
    def isPossible(self, n: int, edges: list[list[int]]) -> bool:
        '''
        Ok, this problem is actually fun and quite easy on the spectrum. 

        So we can only add 0, 1, or 2 edges in the graph. 

        If you tinker around you would notice that if an odd number of edges have odd edges you cannot actually solve the problem because whoever you connect that node will actually make the other node uneven also odd + 2 = odd
        Therfore the first check is it to make sure you have an even number of nodes with odd edges. 

        Next qualifying cases for solving: 
        you can either have 0 odd edges nodes, 2 odd edge nodes, or 4 odd esge nodes


        if you have 0 odd edge nodes: 
            return True you do not need to connect anything 
        
        if you have 2 odd edge nodes: 
            this is what can happen, you can connect those 2 nodes with each other if they are already not connected with each other. 

            or you can find a third common node the both of them are not connected to and then connect the both of them to it. So that node has two more nodes connected to it which keeps the count even and you also get one node each. 

        if you have 4 odd edge nodes: 
            now, you cannot bring any other node in the picture because that would exhaust 2 of the connections allowed. So you must find a match within these. 

            You can try 
            ab cd
            ac bd
            ad bc

            since not directed this should work 

        Okie so linear time complexity, taking space for adj list pretty basic. 
        Ah what a cute problem! 

        Now let's code! 

        Time Complexity: O(n + e) where n is the number of nodes and e is the number of edges
        Space Complexity: O(n + e) where n is the number of nodes and e is the number of edges
        '''
        adj = defaultdict(set)

        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        count = 0
        oddNodes = []
        for node, lst in adj.items():
            if len(lst) % 2 != 0:
                count += 1
                oddNodes.append(node)
        
        if count == 0:
            return True 

        if count not in (2, 4):
            return False
        
        if count == 2:
            a = oddNodes[0]
            b = oddNodes[1]

            # since it is an undirected just need to check one connection and that should solve for us 
            if b not in adj[a]:
                return True 
            
            for i in range(1, n + 1):
                if i != a and i != b and i not in adj[a] and i not in adj[b]:
                    return True 
            
            return False
        
        if count == 4:
            a = oddNodes[0]
            b = oddNodes[1]
            c = oddNodes[2]
            d = oddNodes[3]

            # need to try cases ab cd, ac bd, ad bc
            if ((a not in adj[b] and c not in adj[d]) or 
            (a not in adj[c] and b not in adj[d]) or
            (a not in adj[d] and b not in adj[c])) :
                return True 
        
        return False 
            
        