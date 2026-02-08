# LeetCode Problem Link: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# LeetCode Problem: 329. Longest Increasing Path in a Matrix
# Category: Depth-First Search, Dynamic Programming, Matrix


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''
        brute force solution, from ewch cell run a path traversla like a dfs and then go ahead and get the path count keep with max. 
        Let's code and see if we can atlaeats pass the 3 cases

        to make it better lets think of a DP solution, for each of it what is changing i and j 
        so we need a 2D dp with i and j value sok 
        go ahead build it and that way you wou;ld not need to compute it multiple times. 

        dp[i][j] = length of the maximum path from that number or cell 

        """
Longest Increasing Path in a Matrix - Complexity Summary

Brute-force DFS:
- Idea: Start DFS from every cell, exploring all 4 directions, keeping track of strictly increasing paths.
- Time Complexity: O(4^(m*n)) 
    - Exponential in the number of cells because every possible path combination is explored.
- Space Complexity: O(m*n) 
    - Recursion stack + visited set for each DFS path.

Optimized DFS + Memoization:
- Idea: Use a memo table dp[i][j] to store the length of the longest increasing path starting at (i,j).
  Reuse this result whenever the same cell is visited again in another DFS.
- Time Complexity: O(m * n)
    - Each cell is computed exactly once; each DFS explores at most 4 neighbors.
- Space Complexity: O(m * n)
    - Memo table + recursion stack worst-case depth.

Key Takeaways:
- Brute-force works conceptually but is too slow for large grids.
- Memoization reduces exponential recomputation to linear in the number of cells.
- Recognize overlappin

        '''
        n = len(matrix)
        m = len(matrix[0])
        self.answer = 1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        grid = matrix 
        dp = [[-1 for j in range(m)] for i in range(n)]


        def dfs(i, j, visited):
            # mark visited

            if dp[i][j] != -1:
                return dp[i][j]

            visited.add((i,j))
            max_len = 1  # path length = at least the cell itself

            for di, dj in directions:
                ni, nj = i+di, j+dj
                if (0 <= ni < n and 0 <= nj < m 
                    and (ni,nj) not in visited 
                    and matrix[ni][nj] > matrix[i][j]):
                    max_len = max(max_len, 1 + dfs(ni, nj, visited))
            
            visited.remove((i,j))  # backtrack
            dp[i][j] = max_len
            return dp[i][j]



        for i in range(n):
            for j in range(m):
                self.answer = max(self.answer, dfs(i, j, set()))
        
        return self.answer 


# CORRECT APPROACH:
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # NOTE: THIS IS THE BRUTE FORCE SOLUTION. YOU DO NOT NEED A VISISTED FOR THIS QUESTION BECAUSE THE GREATER THAN PART OF THE QUESTION WILL TAKE CARE OF IT
        # THE TC FOR THIS BRUTE FORCE SOLTUION IS: O(n*m * 4^n)
        # Ok, the 4^n comes from the fact that in the dfs for each cell in the path u visit 4 directions
        # the n*m part comes simply from the fact that u are visiting each cell 
        # ok.
        # Now, when u do a DP
        # for each cell in the DFS u are just checking 4 directions so it becomes 4
        # and totoal TC become O(4*n*m) =O(n*m)
        # easy peasy lemon squeexyyyyyyyyyyy
        # TC: O(n*m) for the DP solution, where n and m are the dimensions of the matrix. Each cell is computed once, and each DFS explores at most 4 neighbors.
        # Space Complexity: O(n*m) for the DP table and O(n*m) for the recursion stack in the worst case (when the path takes us through all cells in a linear manner
        n = len(matrix)
        m = len(matrix[0])
        answer = 1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        dp = [[-1 for _ in range(m)] for _ in range(n)]


        def pathLength(i, j):
            if dp[i][j] != -1:
                return dp[i][j]

            length = 1

            for dr, dc in directions:
                nr = dr + i 
                nc = dc + j 

                if nr in range(n) and nc in range(m) and matrix[nr][nc] > matrix[i][j]:
                    length = max(length, 1 + pathLength(nr, nc))

            dp[i][j] = length
            return dp[i][j]
            
        

        for i in range(n):
            for j in range(m):
                pL = pathLength(i, j)
                if pL > answer:
                    answer = pL

        return answer
