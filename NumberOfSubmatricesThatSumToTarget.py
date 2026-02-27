# LeetCode Problem Link: https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
# LeetCode Problem: 1074. Number of Submatrices That Sum to Target
# Category: Array, Hash Table, Prefix Sum
# Difficulty: Hard


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        '''
        This is a hard problem, lots to think about. You are essentially looking for subarrays which can be a box or rectangle both. 

        This problem build off from leetcode 560, which is number of subarray sums that equal k. 

        In this question the main story is that u keep an anchor which is ur starting row and starting column from there u get all sizes, u keep on foin this. Now the up and down of a column tell u the sum of that entire square subarray u have.

        In the rows or the cells u also store the subarray sum till that point, so vertically adding it up helps. Note that we do not start from 0 while filling the row sum cause the number at 0 index ka sum is that number there is nothing previously. 

        Ok, next thing when u change ur anchor, u have to subtract the previous matric number from it cause remeber u changed ur startung point. 

        See codestorywithmik again for reference.

        time complexity: O(cols^2 * rows) where cols is the number of columns in the matrix and rows is the number of rows in the matrix. This is because we are iterating through all pairs of columns and for each pair, we are iterating through all rows to calculate the sum and check for subarrays that equal the target.
        space complexity: O(rows) for the hashmap that stores the cumulative sums and their frequencies for each pair of columns. In the worst case, the hashmap can store a cumulative sum for each row
        '''
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(1, cols):
                # here starting from 1 cause the sum at the 0th column will be that number itself 
                matrix[i][j] += matrix[i][j - 1]
        
        result = 0
        # now here the leetcode 560 logic is used
        for startingCol in range(cols):
            for j in range(startingCol, cols):
                mp = {}
                currSum = 0 #note this is now the vertical, oopar neeche wala sum 
                mp[0] = 1
                for row in range(rows):
                    currSum += matrix[row][j]
                    if startingCol > 0:
                        currSum -= matrix[row][startingCol - 1]
                    diff = currSum - target
                    if diff in mp:
                        result += mp[diff]
                    mp[currSum] = mp.get(currSum, 0) + 1
        return result 
