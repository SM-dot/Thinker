# Leetcode 1615. Maximal Network Rank
# https://leetcode.com/problems/maximal-network-rank/
# Category: Graph, DFS, BFS - but no actual graph traversal algorithm is needed
class Solution:
    '''
    Simply follow the instrcutions of the question. Rank means the number of edges or roads
    from any country or node. This simply translates to indegrees/ outdegrees of the node which can 
    be calculated by just iterating over the edges. 

    Then, as mentioned in the question. For every pair of nodes, calculate the rank
    rank = sum of x and y nodes
    However, if x and y are connected - we would be counting the connected edge twice
    thus -1 from the rank and keep track of maximum. 

    Now, let's code!
    T.C: o(n^2 + m) where n is the number of nodes and m is the number of edges
    S.C: O(n + m) for the rank and connected set
    '''
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        rank = defaultdict(int)
        connected = set()
        for a, b in roads:
            rank[a] += 1
            rank[b] += 1
            connected.add((a, b))
            connected.add((b, a))
        
        maxRank = 0
        for i in range(n):
            for j in range(i + 1, n):
                currRank = rank[i] + rank[j]
                if (i, j) in connected: 
                    maxRank = max(maxRank, currRank - 1)
                else:
                    maxRank = max(maxRank, currRank)
        return maxRank 