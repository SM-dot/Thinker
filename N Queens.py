# Leetcode 51: N-Queens
# https://leetcode.com/problems/n-queens/
# Category: Backtracking, Recursion


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        '''
        So this is actually a recursion and backtracking question. 
        Think of it like this, actually think super simple here. 
        You try each position on the board for the queen. So you fix one position and then go ahead and start filling the board from the top. Once you fill it from the top you check if this config makes sense. If it does good, add it. Otherwise undo the changes u made and go ahead and explore other positions. 

        There are two approaches to this

        Mainly differing in the wya you check if a position is valid or not.

        What do you mean by if a position is valid or not - simply means that can any other queen kill it or not. 
        You check upward, right diagonal, left diagonal and thats it. Not bottom cause u are filling it from the top. 

        This validation u can do in two ways which drives the two different approaches and bring the time complexity down. The time complexity is still rpetty high for this one. 

        If you do loops check up, right side, left side. And then do it this will take n time 

        if you store that oh in a column I put something and then go ahead and code it up then that reduced it to O(1)

        the most beautiful thing about approach 2 is that in approach 2: 
        to see if something is in the right or left diagonal u simply have to see the sum of the indexes to know if something is ont he right or left 
        see codestorwithmik for this. 

        time complexity: O(N!) where N is the number of queens to be placed on the board. This is because we are exploring all possible configurations of placing N queens on an N x N chessboard, and in the worst case, we may have to explore all permutations of queen placements.
        space complexity: O(N) for the recursion stack and the sets used to track the columns

        Ok, now lets code it up. 
        '''
        # step 1 is to create the board for it 
        board = [["."] * n for _ in range(n)] #VIP: Strings are immutable in Python so have to do like this, operate and then when appending to result modify it accordingly. 
        result = []
        cols = set()
        rightDiag = set() 
        leftDiag = set()

        # we  will be filling it row wise 
        def solve(row):
            if row >= n: 
                result.append([''.join(r) for r in board])

            
            for col in range(n):
                rightDiagID = row + col
                leftDiagID = row - col
                if col in cols or rightDiagID in rightDiag or leftDiagID in leftDiag:
                    continue # we know that this position will be killed
                
                cols.add(col)
                rightDiag.add(rightDiagID)
                leftDiag.add(leftDiagID)
                board[row][col] = 'Q'

                solve(row + 1)

                cols.remove(col)
                rightDiag.remove(rightDiagID)
                leftDiag.remove(leftDiagID)
                board[row][col] = '.'
        
        solve(0)
        return result 







