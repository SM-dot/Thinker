# Leetcode Link: https://leetcode.com/problems/where-will-the-ball-fall/description/
# Problem Number: 1706
# Category: Arrays - medium (breaking the problem down)

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        '''
        Break the problem down. Think when is the ball stuck, when can it move? 

        If the cell is 1: (means the ball moves to the right down cell)
            and the cell right next to it is -1 then ball is stuck
            or the next column is the boundary, this means it wont fall anywhere 
        If the cell is -1: (means the ball moves to the left down cell)
            and the cell before it or left to it is +1 then ball is stuck
            or the next column to the left is boundary => col == 0 then stuck
        whenever stuck, flag it and quit the journey 
        once you have quit the journey then in resultant list store -1 
        if flag is false (means the ball falls) in the resultant list add the column

        Let's get coding!
        '''
        n = len(grid)
        m = len(grid[0])
        answer = []

        for ball in range(m):
            # ball dropping starts from the top row, the ball that is being dropped is same as column number initially
            row = 0 
            col = ball
            stuck = False
            while (row < n and col < m):
                if grid[row][col] == 1:
                    if (col == m - 1 or grid[row][col + 1] == -1):
                        stuck = True
                        break
                    # not stuck 
                    col += 1
                else:
                    if (col == 0 or grid[row][col - 1] == 1):
                        stuck = True
                        break
                    # not stuck
                    col -= 1
                row += 1

            if stuck:
                answer.append(-1)
            else:
                answer.append(col)
        
        return answer
