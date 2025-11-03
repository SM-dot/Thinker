# Leetcode Link: https://leetcode.com/problems/rotting-oranges/
# Category: BFS, Graphs 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        rotten_oranges = deque()
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        count = 0    
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 1
        if count == 0:
            return 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    rotten_oranges.append((i, j))
                    visited.add((i, j))
        
        
        time_elapsed = 0
        while rotten_oranges:
            k = len(rotten_oranges)
            for i in range(k):
                rotten_r, rotten_c = rotten_oranges.popleft()

                for del_r, del_c in directions: 
                    new_r = del_r + rotten_r
                    new_c = del_c + rotten_c

                    if new_r in range(n) and new_c in range(m) and (new_r, new_c) not in visited and grid[new_r][new_c] == 1:
                        rotten_oranges.append((new_r, new_c))
                        grid[new_r][new_c] = 2
                        visited.add((new_r, new_c))
            time_elapsed += 1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1 
        return time_elapsed - 1

 
# REV october 10th, 2025 