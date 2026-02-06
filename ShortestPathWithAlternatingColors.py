#LeetCode Problem Link: https://leetcode.com/problems/shortest-path-with-alternating-colors/
#LeetCode Problem: 1129. Shortest Path with Alternating Colors
#Category: Graph, Breadth-First Search
#Difficulty: Medium


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # create a q and put 0, nocolor in it 
        # create an adj which has the nextNode and the color 
        # from your 0th node go to the other nodes and note it down it in the result 
        # if color matches prev color put -1 in the result
        # do not explore that path further
        # only put paths that have different colors 
        # from that see all the other edges, store the color of the edge 
        # Time Complexity: O(V + E), where V is the number of vertices (nodes) and E is the number of edges (redEdges + blueEdges). Each node and edge is processed at most once.
        # Space Complexity: O(V + E), for storing the adjacency list and the queue in the worst case.
        from collections import defaultdict, deque
        result = [float('inf')] * n

        adj = defaultdict(list)
        q = deque()
        # going to store pairs (node, color, steps)
        # 'x' => starting color, 'r' => red color, 'b' => blue color

        for u,v in redEdges:
            adj[u].append((v, 'r'))
        
        for u,v in blueEdges:
            adj[u].append((v, 'b'))

        q.append((0, 'x', 0)) 
        visited = set()
        visited.add((0, 'x')) # WE NEED TO ADD COLOR HERE AS THAT IS AN IMPORTANT DIFFERENTIATOR


        while q:
            n = len(q)
            for _ in range(n):
                node, color, steps = q.popleft()
                if result[node] > steps:
                    result[node] = steps
                

                for nextNode, nextColor in adj[node]:
                    if nextColor != color and (nextNode, nextColor) not in visited:
                        q.append((nextNode, nextColor, steps + 1))
                        visited.add((nextNode, nextColor))


        for i, num in enumerate(result): 
            if num == float('inf'):
                result[i] = -1
        
        return result 

