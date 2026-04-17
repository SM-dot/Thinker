class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        Main trik here is to see what happens when u transpose the original matrix. The transpose basically makes the first row the first column. 

        so you will have something like this when you transpose the original matrix 
        1 4 7
        2 5 8 
        3 6 9 

        ok and notice that the transpose of a matrix is just flipping the matrix along the diagonal. and the code is just matrix[i][j] = matrix[j][i] - rememeber this tiny trick it will help in the future 


        Ok, now next step is to just reverse the entire row 
        so 1 4 7 now becomes 4 7 1 see how that matches the top row, keep on doing this and then you have the answer

        time complexity: O(n^2) where n is the number of rows (or columns) in the input matrix. This is because we are iterating through each element of the matrix twice: once for transposing and once for reversing the rows.
        space complexity: O(1) since we are modifying the matrix in-place and not using any additional data structures that grow with the input size.
        
        """
        n = len(matrix)
        m = len(matrix[0])

        # transposing the matrix here 
        for i in range(n):
            for j in range(i, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # now time to reverse each row 
        for i in range(n):
            left = 0
            right = n - 1

            while left < right: 
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1
            
        