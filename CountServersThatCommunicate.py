# Leetcode Link: https://leetcode.com/problems/count-servers-that-communicate/
# Leetcode Problem: 1267. Count Servers that Communicate
# Category: Array, Hash Table, Matrix
# Difficulty: Medium


# Brute Force Approach using HashSet
# Time Complexity: O(m * n), where m is the number of rows and n is the number of columns in the grid.
# Space Complexity: O(m + n) for storing the row and column mappings.

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rowMap = defaultdict(list)
        colMap = defaultdict(list)

        rows = len(grid)
        cols = len(grid[0])


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    rowMap[i].append((i, j))
                    colMap[j].append((i, j))
        

        # row comms:
        comms = set()
        for k,v in rowMap.items():
            if len(v) > 1:
                for servers in v:
                    comms.add(servers)
        
        for k,v in colMap.items():
            if len(v) > 1:
                for servers in v:
                    comms.add(servers)
        
        return len(comms)


# Optimized Approach without using extra space for row and column mappings
# Time Complexity: O(m * n), where m is the number of rows and n is the number of columns in the grid.
# Space Complexity: O(m + n) for storing the row and column counts.

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        rowMap = [0] * rows
        colMap = [0] * cols


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    rowMap[i] += 1
                    colMap[j] += 1
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (rowMap[i] > 1 or colMap[j] > 1):
                    count += 1
        
        return count
