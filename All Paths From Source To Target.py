# leetCode 797. All Paths From Source to Target
# Problem Link: https://leetcode.com/problems/all-paths-from-source-to-target/
# Category: Graph, Backtracking, Depth-First Search

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        '''
        Input: Directed Acyclic Graph (DAG) represented as an adjacency list
        Operations:     
        - Start from node 0 and explore all paths to the target node (last node)
        - Use DFS to explore each path, keeping track of the current path
        - When the target node is reached, add the current path to the result list
        Output: List of all paths from source (node 0) to target (last node)
        T.C: O(2^N * N) in the worst case, where N is the number of nodes
        S.C: O(N) for the recursion stack and path storage  
        Using DFS traverse all possible paths
        '''
        answer = []
        destination = len(graph) - 1
        
        def dfs(node, path):
            path.append(node)
            if node == destination: 
                answer.append(path[:])
                path.pop()
                return 

            for nextNode in graph[node]:
                dfs(nextNode, path)
            
            path.pop()
            
            
            
        dfs(0, [])
        return answer 

            