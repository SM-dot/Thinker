## LeetCode 417. Pacific Atlantic Water Flow
# Problem Link: https://leetcode.com/problems/pacific-atlantic-water-flow/  
# Cateogory: BFS, DFS, Graph
# Free on Neetcode.io

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        Input: Grid
        Output: Modified grid with each cell distance to the chest
        '''
        n = len(grid)
        m = len(grid[0])

        # Chest coordinates
        chest = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    chest.append((i, j))
        
        def explore(i, j):
            '''
            Input: coordiantes of grid
            Output: None
            BFS to find closest disatnce from chest
            '''
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            q = deque()
            q.append((i, j))
            visited = set()
            distance = 1

            while q:
                x = len(q)
                for _ in range(x):
                    iC, jC = q.popleft()

                    for dx, dy in directions:
                        newX = dx + iC
                        newY = dy + jC
                        if newX in range(n) and newY in range(m) and (newX, newY) not in visited and grid[newX][newY] > distance and grid[newX][newY] not in {0, -1}:
                            grid[newX][newY] = distance
                            q.append((newX, newY))
                            visited.add((newX, newY))
                distance += 1



        
        # Finding distances from all chests
        for i, j in chest: 
            explore(i, j)