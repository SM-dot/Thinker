# Leetcode Link: https://leetcode.com/problems/number-of-operations-to-make-network-connected/
# Category: Graphs, BFS, DFS, DSU (Optional)

# APPROACH 1
'''
for n nodes to be all connected you need atleast n -1 edges
for example 3 nodes, all are connected by 2 edges
Basically need to find how many components or nodes are all connected together and we can do this by a simple DSU 
where we see if the nodes are not in the same set, we go ahead and add them in the set and the number of components/ start nodes we had decreases 

Once we have grouped all the nodes, we would have components left. Then the answer would just be components - 1 cause thats the number of nodes we need to connect n components

In case it is not possible to connect all nodes, this check will be at the start of the code becuase if we have less than n - 1 edges means it is not possible to solve the problem! 

Please note: this problem can also very simply be solved with a DFS/BFS 
'''
class DSU: 
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
    
    def find(self, i):
        if i == self.parents[i]:
            return i
        self.parents[i] = self.find(self.parents[i])
        return self.parents[i]
    
    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent == y_parent:
            return 
        
        if (self.rank[x_parent] > self.rank[y_parent]):
            self.parents[y_parent] = x_parent
        
        elif (self.rank[y_parent] > self.rank[x_parent]):
            self.parents[x_parent] = y_parent
        
        else:
            self.parents[x_parent] = y_parent
            self.rank[y_parent] += 1
        
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        dsu = DSU(n)
        components = n

        if len(connections) < n - 1:
            return -1 
            
        for edge in connections:
            u = edge[0]
            v = edge[1]
            if (dsu.find(u) != dsu.find(v)):
                components -= 1
                dsu.union(u, v)
        return components - 1

# APPROACH 2
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        visited = set()
        adj = defaultdict(list)

        if len(connections) < n -1:
            return -1
        components  = 0
        for edge in connections:
            u = edge[0]
            v = edge[1]
            adj[u].append(v)
            adj[v].append(u)

        def dfs(i):
            if i in visited:
                return 
            visited.add(i)
            for nextNode in adj[i]:
                dfs(nextNode)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1

        return components -1 

