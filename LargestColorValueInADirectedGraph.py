# leetcode Link: https://leetcode.com/problems/largest-color-value-in-a-directed-graph/description/
# Category: Graphs, DFS, BFS 
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # ok can be done by DFS OR BFS(topological sort)
        # key idea: the previous node has an array of frequency of colors which will tell u max frequency till that node and the frequency of colors ur node has - modify it with the max and update with current color node. 
        # Building a 2-D grid of sorts 
        # The answer will be the frequency of any node at any point 
        # Using Kahn's algo here - why? toposort using Kahn's algo will also help us detect a cycle
        # Indegree of the nodes will give us a good starting point
        # Now let's code!

        adj = defaultdict(list)
        n = len(colors)
        answer = -1
        indegrees = [0] * n
        for u, v in edges: 
            adj[u].append(v)
            indegrees[v] += 1
        
        q = deque()
        colorFreq = [[0] * 26 for i in range(n)]
        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                q.append(i)
                color = ord(colors[i]) - ord('a')
                colorFreq[i][color] = 1
        
        # to detect a cycle 
        count = 0
        while q: 
            element = q.popleft()
            count += 1
            answer = max(answer, colorFreq[element][ord(colors[element]) - ord('a')])

            for nei in adj[element]:
                for i in range(26):
                    colorFreq[nei][i] = max(colorFreq[nei][i], colorFreq[element][i] + (1 if i == ord(colors[nei]) - ord('a') else 0))

                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
        
        if count < n:
            return -1
        return answer 
