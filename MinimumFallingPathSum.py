# LeetCode Problem Link: https://leetcode.com/problems/minimum-falling-path-sum/
# LeetCode Problem: 931. Minimum Falling Path Sum
# Category: Dynamic Programming, Matrix


'''
Explanation: 
First start with a simple recurisve solution. For each cell in the first row, get the minimum path sum from that cell to the bottom row. The minimum path sum from a cell is the value of that cell plus the minimum of the path sums from the three possible cells in the next row (the cell directly below, the cell below and to the left, and the cell below and to the right).
Then, we can optimize this recursive solution using dynamic programming. We can create a dp array where dp[i][j] represents the minimum path sum from cell (i, j) to the bottom row. We can fill this dp array starting from the second to last row and moving upwards, using the same logic as in the recursive solution. Finally, the answer will be the minimum value in the top row of the dp array.

Recursive solution time complexity: O(3^n) where n is the number of rows, because from each cell we have 3 choices for the next step.
Dynamic programming solution time complexity: O(n*m) where n is the number of rows and m is the number of columns, because we fill a dp array of size n*m.

'''
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = matrix[-1].copy()

        for row in range(len(matrix) - 2, -1, -1):
            new_dp = [None] * len(matrix[0])
            for col in range(len(matrix[0])):
                min_path = dp[col]
                
                if col > 0 and dp[col-1] < min_path:
                    min_path = dp[col-1]
                if col < len(matrix[0]) - 1 and dp[col+1] < min_path:
                    min_path = dp[col+1]

                new_dp[col] = matrix[row][col] + min_path
            dp = new_dp

        return min(dp)