# LeetCode Problem Link: https://leetcode.com/problems/max-area-of-island/
# LeetCode Problem: 695. Max Area of Island
# Category: Array, Depth-First Search, Breadth-First Search, Matrix
# Difficulty: Medium

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # whenever I find a 1 and that has not been visited I will go and visit those land cells in that island and compare to the max land cells i have seen so far. 
        # for visiting the cells in an island can do bfs and dfs both 
        # no particular choice, if we know that are lands are most spreak maybe then doing a bfs is faster as comapre to dfs 
        # for visiting we can either keep a set of data which has visited cells or modeify the ecisiting cell
        # O(N) TC
        # SC: O(1)
        # Now let's code 


        n = len(grid)
        m = len(grid[0])
        self.maxLand = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def landArea(i, j):
            if i not in range(n) or j not in range(m) or grid[i][j] != 1:
                return 0 
            sum = 1 
            grid[i][j] = "#"
            for dr, dc in directions: 
                nr = i + dr
                nc = j + dc
                 
                sum += landArea(nr, nc)
            
            return sum 

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    self.maxLand = max(self.maxLand, landArea(i, j))
        
        return self.maxLand
