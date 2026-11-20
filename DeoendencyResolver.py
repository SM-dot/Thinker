# James Peralta 75 list, couldnt really find it on leetcode
# Link: https://leetcode.com/problems/dependency-resolver/

from collections import defaultdict, deque 
def can_resolve(dependencies: list) -> bool:
    """Return True when every dependency can be satisfied."""
    # Write your solution here
    # seems to be a toposort problem, if there is a cycle then we remove it
    # time complexity is O(n) and space complexity is O(n) as well.
    # optimal solution would be to use a DFS and check for cycles, but this is a more intuitive approach.
    
    adj = defaultdict(list)
    indegrees = {}

    for a,b in dependencies: 
        adj[b].append(a)

        if b not in indegrees:
            indegrees[b] = 0
        
        if a not in indegrees:
            indegrees[a] = 0

        indegrees[a] += 1
        if a == b:
            return False 
    
    q = deque()

    for node, val in indegrees.items():
        if val == 0:
            q.append(node)
    
    result = []
    while q:
        node = q.popleft()
        result.append(node)

        for nextNode in adj[node]:
            indegrees[nextNode] -= 1
            if indegrees[nextNode] == 0:
                q.append(nextNode)
    
    if len(result) == len(adj):
        return True 
    
    return False 
