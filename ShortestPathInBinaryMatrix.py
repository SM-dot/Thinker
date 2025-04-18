# Leetcode link: https://leetcode.com/problems/shortest-path-in-binary-matrix/
# Category: Graphs, BFS, Dijkstras 
'''
Can be solved with BFS(as all weights are 1 ) and Dijkstras 
'''
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = deque()
        q.append((0, 0))
        visited = set()
        visited.add((0, 0))
        n = len(grid)
        levels = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]

        if grid[0][0] == 1:
            return -1 

        while q: 
            for i in range(len(q)):
                r, c = q.popleft()
                if r == n-1 and c == n-1:
                    return levels + 1
                
                for dir in directions:
                    new_r = r + dir[0]
                    new_c = c + dir[1]

                    if new_r in range(n) and new_c in range(n) and grid[new_r][new_c] == 0 and (new_r, new_c) not in visited:
                        q.append((new_r, new_c))
                        visited.add((new_r, new_c))
            levels += 1
        return -1
