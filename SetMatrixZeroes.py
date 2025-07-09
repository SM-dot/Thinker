# Leetcode Link: https://leetcode.com/problems/set-matrix-zeroes/description/
# Problem Number: 73
# Category: 2D Matrix 


from typing import List

# OPTIMAL 
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Approach:
        1. Use the first row and first column as markers to track which rows and columns should be set to zero.
        2. Iterate through the matrix, and if a cell is zero, mark the corresponding row and column.
        3. Iterate through the matrix again (excluding the first row and column) and set cells to zero based on the markers.
        4. Handle the first column separately if it contains a zero.
        5. Handle the first row separately if it originally contained a zero.

        Time Complexity: O(M * N), where M is the number of rows and N is the number of columns.
        Space Complexity: O(1), as we are using the matrix itself for marking without additional space.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
              
# BRUTE FORCE:
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Approach:
        1. Use two sets to keep track of rows and columns that need to be set to zero.
        2. Iterate through the matrix, recording row and column indices of zero elements.
        3. Iterate through the matrix again, setting elements to zero if their row or column is in the recorded sets.
        4. This approach ensures we do not modify the matrix while determining which rows and columns need to be zeroed.
        
        Time Complexity: O(M * N), where M is the number of rows and N is the number of columns.
        Space Complexity: O(M + N), since we use additional sets to store row and column indices.
        """
        rows = set()
        cols = set()

        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for i in range(n):
            for j in range(m):
                if i in rows or j in cols:
                    matrix[i][j] = 0



# RV July 8th 2025