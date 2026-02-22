# LeetCode Problem Link: https://leetcode.com/problems/maximum-number-of-k-divisible-components/
# LeetCode Problem: 2518. Maximum Number of K-Divisible Components
# Category: Graph, Depth-First Search, Tree
# Difficulty: Hard 


from collections import defaultdict 
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        '''
        Relatively simpler question acc to submission and online rate. 
        The main idea that helps make this hard easy is that the sum of all the values is k. 
        So you go ahead and build off the sum from the node u are starting, u go ahead and visit all the neighbours from that node, you get the sum of the neighbours from that node, then go ahead and return componenet sum % k, why this? cause if the sum of one of the components is %k u do not want to modify the component. 

        This one can be done using BFS and DFS both

        time complexity: O(n) to build the adjacency list and to do the DFS traversal, space complexity: O(n) for the adjacency list and the recursion stack in the worst case.
        space compelxity: O(n) for the adjacency list and the recursion stack in the worst case.
        '''
        adj = defaultdict(list)
        count = 0

        def dfs(curr, parent):
            nonlocal count
            sum = values[curr]

            for nextNode in adj[curr]:
                if nextNode != parent: 
                    sum += dfs(nextNode, curr)
                    sum %= k 
            
            sum %= k 
            if sum % k == 0:
                count += 1

            return sum


        for a,b in edges: 
            adj[a].append(b)
            adj[b].append(a)
        
        dfs(0, -1)

        return count 
