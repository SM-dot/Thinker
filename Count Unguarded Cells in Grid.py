# Leetcode Name: Count Unguarded Cells in Grid
# Leetcode Link: https://leetcode.com/problems/count-unguarded-cells-in-the-grid
# Category: Array, Matrix, Simulation


class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        '''
        Keep it super simple just do what it says 
        '''
        grid = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        def visit(row, col):
            # up direction
            for r in range(row-1, -1, -1):
                if grid[r][col] not in (2, 3):
                    grid[r][col] = 1
                else:
                    break
            
            # down direction
            for r in range(row + 1, m):
                if grid[r][col] not in (2, 3):
                    grid[r][col] = 1
                else:
                    break
            
            # right direction 
            for c in range(col + 1, n):
                if grid[row][c] not in (2, 3):
                    grid[row][c] = 1
                else:
                    break
            
            # left direction
            for c in range(col - 1, -1, -1):
                if grid[row][c] not in (2, 3):
                    grid[row][c] = 1
                else:
                    break

        # mark all the cells which have a guard
        for r, c in guards: 
            grid[r][c] = 2
        
        # mark all the cells with a wall
        for r, c in walls:
            grid[r][c] = 3
        
        for r, c in guards:
            visit(r,c)
        

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1
        
        return count 
