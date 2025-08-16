# LeetCode 1443. Minimum Time to Collect All Apples in a Tree
# Problem Link: https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/
# Category: Graph, DFS


class Solution:
    '''
    Input: Number of nodes n, edges representing the tree, and a list indicating if each node has an apple
    Operations:
    - Build an adjacency list to represent the tree
    - Use DFS to traverse the tree and calculate the minimum time to collect all apples
    - For each node, if it has an apple or if any of its children have apples, add 2 to the time (1 for going to the child and 1 for returning) 
    Output: Minimum time to collect all apples
    T.C: O(N) where N is the number of nodes in the tree
    S.C: O(N) for the adjacency list and recursion stack
    Using DFS to traverse the tree and calculate the minimum time   
    '''
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node, parent):
            time = 0

            for child in adj[node]:
                if child != parent: 
                    childTime = dfs(child, node)
                    if childTime or hasApple[child]:
                        time += childTime + 2
            return time
        
        return dfs(0, -1)