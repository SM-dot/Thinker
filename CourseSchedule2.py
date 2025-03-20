# Leetcode:https://leetcode.com/problems/course-schedule-ii/
# Problem Number: 210 
# Category: Graphs, Specifically Toposort or Kahn's Algorithm 

# Look at Course Schedule 1 code, very similar approach 
# Now we simply dont just want to detect a cycle but also retrieve the order in which the courses should be taken. 
# If you think about it then while we pop from the q, we are getting the order in which the nodes can be visited. If we store the element we are popping then we also have the order!
# Note: There can be many topological orders, we have to return anyone. 
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for edge in prerequisites:
            u = edge[0]
            v = edge[1]
            adj[v].append(u)
        
        indegrees = [0 for _ in range(numCourses)]
        for i in range(numCourses):
            for v in adj[i]:
                indegrees[v] += 1

        q = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        
        toposort = []
        while q:
            element = q.popleft()
            toposort.append(element)
            for ngbr in adj[element]:
                indegrees[ngbr] -= 1
                if (indegrees[ngbr] == 0):
                    q.append(ngbr)
        
        print(toposort)
        if len(toposort) == numCourses:
            return toposort
        else:
            return []
