# LeetCode Problem Link: https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/
# LeetCode Problem: 1786. Number of Restricted Paths From First to Last Node
# Category: Graph, Depth-First Search, Dijkstra's Algorithm


from collections import defaultdict 
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        '''
        This problem basically has two parts. 
        The first part is to find the shortest path from the 0th node to the last node and then go ahead an aidentify all the nodes that have the shortest distance less than the current node while going to the last node. 

        1. Do dijkstras 
        2. Find all the paths in the graph that lead to the last node such that in that path the diatance tpo the final node is less than the distance for the prev node. 
        For example: 
        blue = dijkstras distance that has been calcualted 
        black = node number 
        we need to find paths where blue is decreasing while moving to th elast node. Easy peasy lemon squeezy? Nope not at all, why cause there could be multiple paths and that could lead to a slower solution. 

        First let's implement dijkstras and then see what to do. 

        Time Complexity: O(E log V) for Dijkstra's algorithm, where E is the number of edges and V is the number of vertices. The DFS to count restricted paths can take O(V + E) in the worst case, leading to an overall complexity of O(E log V + V + E).
        Space Complexity: O(V + E) for storing the graph and the recursion stack in the worst case.
        '''
        adj = defaultdict(list)
        mod = 10**9 + 7

        for u, v, w in edges:
            adj[u].append((v,w))
            adj[v].append((u, w))
        
        # Dijkstras till here 
        result = [float('inf')] * (n + 1)
        result[0] = 0
        result[n] = 0
        pq = []
        # distance, node 
        heapq.heappush(pq, (0, n))

        while pq:
            distance, node = heapq.heappop(pq)

            for nextNode, nextDistance in adj[node]:
                newDistance = nextDistance + distance
                if result[nextNode] > newDistance:
                    heapq.heappush(pq, (newDistance, nextNode))
                    result[nextNode] = newDistance 
        
        # now finding the numbe rof restricted paths that exist 
        dp = [-1] * (n + 1)  # dp[node] = number of restricted paths from node to n
        dp[n] = 1  # base case

        def dfs(node):
            if dp[node] != -1:
                return dp[node]
            
            res = 0
            for nextNode, weight in adj[node]:
                if result[nextNode] < result[node]:
                    res += dfs(nextNode)
            
            dp[node] = res
            return dp[node] 
        
        return dfs(1) % mod