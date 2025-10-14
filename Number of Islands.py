# leetcode 200. Number of Islands
# Link: https://leetcode.com/problems/number-of-islands/
# Difficulty: Medium

'''
Explanation:
Given a 2D grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Time Complexity: O(n * m) where n is the number of rows and m is the number of columns in the grid. This is because we potentially visit each cell in the grid once during the DFS traversal.
Space Complexity: O(n * m) in the worst case, which occurs when the grid is filled with land ('1's). In this case, the recursion stack for DFS can go as deep as n * m. In the average case, the space complexity is O(min(n, m)) due to the recursion stack.
'''


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        visited = set()

        def dfs(i, j):
            if i not in range(n) or j not in range(m) or (i, j) in visited or grid[i][j] != "1":
                return 
            visited.add((i, j))
            for dr, dc in directions:
                row = dr + i
                col = dc + j
                dfs(row, col)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(i, j)
                    count += 1
        
        return count 