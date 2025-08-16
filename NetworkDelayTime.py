# LeetCode 743. Network Delay Time
# Problem Link: https://leetcode.com/problems/network-delay-time/
# Category: Graph, Dijkstra's Algorithm 

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        Direct implementation of dijkstras algo
        weight == time for this problem
        Steps:
        1. Build your adjacency list
        2. Add start node in priority q {distance, source}
        3. traverse and add distances in resultant array which have smaller distance than current distance. NOte that initially everything is at an infinit distance from the starting node
        4. Return the max number from the result array 
        T.C: E log V
        S.C: V + E
        where E = edges and V = vertices or nodes 
        '''
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        
        result = [float('inf') for _ in range(n + 1)] # stores the distance from the starting node to each node
        result[k] = 0
        result[0] = 0 # cause no 0 node in this question
        pq = [(0, k)]

        while pq:
            distance, node = heapq.heappop(pq)

            for nextNode, weight in adj[node]:
                new_distance = weight + distance
                if result[nextNode] > new_distance:
                    result[nextNode] = new_distance
                    heapq.heappush(pq, (new_distance, nextNode))
        
        return max(result) if float('inf') not in result else -1
