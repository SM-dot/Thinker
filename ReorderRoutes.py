# Leetcode Link: https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/
# Category: Graphs 
'''
Basically store the real edges as 1 u -> v
and also tore v -> u which is a fake edge as 0
so your adjacency list will look something like this: 
node: 
1 -> [[2, 0], [3, 1]]
2 -> [[1, 1]]
3 -> [[1, 0]]
this is done so that we can visit ALL nodes and not just the ones based on the current direction

Start your traversal which can be DFS or BFS 
Next you will notice that if you reach a node in your traversal and if that edge is real, you will know through the second value in the list. Then you know that since we started from 0 and reached this node it means that the directi0on was away from the 0th node thus add 1 to the answer. 
If you reach a node and if it is a fake edge, means that the real edge is pointing towards 0 so all GOOD. 
Here using DFS, ommiting the visited set by keeping track of the parent. 
Time Complexity: O(n)
'''
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in connections: 
            adj[u].append((v, 1))
            adj[v].append((u, 0))
        answer = 0
        
        def dfs(node, parent):
            nonlocal answer 
            for nextNode, path in adj[node]:
                if nextNode != parent:
                    if path == 1:
                        answer += 1
                    dfs(nextNode, node)
        dfs(0, -1)
        return answer 
        
