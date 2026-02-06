# LeetCode Problem Link: https://leetcode.com/problems/unique-paths-iii/
# LeetCode Problem: 980. Unique Paths III
# Category: Backtracking, Depth-First Search, Matrix


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        '''
        Think simply
        This is a classic backtracking or dfs solution. 

        1. First know how mnay non obstacles blocks u have 
        2. Add one to the above cause the starting point in not an obstacle 
        3. When u are doing 1 also find ur starting point 
        4. once have all of them then go ahead and start ur backtracking algorithm 
        5. this is gonna be a regular dfs
        def backtarcking(count, i, j):
            here count is gonna be the number of non obstacles u have seen so far 
            if u reach ur target and nonobstacles == count u add 1 to the answer otherqise u return 
            regular exploration, out of bounds etc. 
            Note u have to backtrack here cause very obviously u have multiple paths to explore. 
            Ok, now moving on - you do not need to have a visited set here, as u go mark the cell as -1 mean u cannot come back to it. this saves on space. 

            Note time complexity: 
            so basically for each cell u can move in 3 directions. Why 3? 
            Cause th2 4th direction would be where u are coming from. Therefore the time compelxity is gonna be 3^(n + m)

            Space complexity: o(m + n) for the recursion stack, in the worst case when the path takes us through all cells in a linear manner.
            Think aboou this. This is definetely gonna come from the recursion path and not the regular path cause we are not using any explicit new memory fopr our code. 
            Ok now let's code!!! 
        '''
        n = len(grid)
        m = len(grid[0])
        nonObstacles = 1
        startingPoint_x = 0
        startingPoint_y = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    nonObstacles += 1
                if grid[i][j] == 1:
                    startingPoint_x = i
                    startingpoint_y = j
        
        self.answer = 0
        def dfs(i, j, count):
            if i not in range(n) or j not in range(m) or grid[i][j] == -1:
                return 
            
            if grid[i][j] == 2:
                if count == nonObstacles:
                    self.answer += 1
                return 
            
            grid[i][j] = -1
            for dr, dc in directions: 
                ni = i + dr
                nj = j + dc
                dfs(ni, nj, count + 1)
            grid[i][j] = 0
        
        dfs(startingPoint_x, startingPoint_y, 0)
        return self.answer 
