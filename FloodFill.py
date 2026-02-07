# LeetCode Problem Link: https://leetcode.com/problems/flood-fill/
# LeetCode Problem: 733. Flood Fill
# Category: Depth-First Search, Breadth-First Search, Matrix
# Difficulty: Easy

'''
Explanation:
To perform a flood fill on a given image starting from a specific pixel, we can use either
a depth-first search (DFS) or a breadth-first search (BFS) approach. The idea is to change the color of the starting pixel and then recursively or iteratively change the color of all connected pixels that have the same original color.

time complexity: O(n*m) in the worst case, where n is the number of rows and m is the number of columns in the image. This happens when all pixels are connected and have the same color as the starting pixel.
space complexity: O(n*m) in the worst case for the recursion stack in DFS or the
'''
class Solution:
    
    def dfs(self, i, j, visited, color, grid, start_color):
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        n = len(grid)
        m = len(grid[0])
        if (i, j) in visited or i not in range(n) or j not in range(m) or grid[i][j] != start_color:
            return 
        
        visited.add((i, j))
        grid[i][j] = color
        for dir in directions: 
            r = i + dir[0]
            c = j + dir[1]
            self.dfs(r, c, visited, color, grid, start_color)
        return 
        



    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        visited = set()
        self.dfs(sr, sc, visited, color, image, start_color)
        return image
        