# Leetcode Link: https://leetcode.com/problems/course-schedule
# Problem Number: 207 
# Category: Graphs and Topological Sorting to be specific 
# The basic idea is that you need some ordering of all the courses.
# If there is a cycle in the ordering, it means you cannot finish the courses.

# Step 1: Create an adjacency list (graph representation).
# Step 2: Perform topological sorting.

# There are two ways to do this:
# 1. BFS (Kahn's Algorithm) - Count the number of nodes in the topological sort.
#    If the number of nodes in the sorted order matches the total number of courses, it is possible to finish them.
# 2. DFS - Use a visited set and a recursive stack. If a visited node is also in the recursive stack, it indicates a cycle.

# This solution uses BFS (Kahn's Algorithm) for topological sorting.
# Kahn's Algorithm:
# - Count indegrees for each node.
# - Only enqueue nodes with an indegree of 0.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        count = 0
        for edge in prerequisites: 
            a = edge[0]
            b = edge[1]
            adj[b].append(a)

        indegrees = [0 for i in range(numCourses)]
        for i in range(numCourses):
            for v in adj[i]:
                indegrees[v] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        
        while q:
            element = q.popleft()
            count += 1
            for ngbr in adj[element]:
                indegrees[ngbr] -= 1
                if indegrees[ngbr] == 0:
                    q.append(ngbr)

        if count == numCourses:
            return True 
        return False 

