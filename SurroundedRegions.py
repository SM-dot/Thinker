# LeetCode Problem Link: https://leetcode.com/problems/surrounded-regions/
# LeetCode Problem: 130. Surrounded Regions
# Category: Array, Depth-First Search, Breadth-First Search, Union Find,


# Time Complexity: O(N * M) where N is the number of rows and M is the number of columns in the board.
# BFS/DFS traversal takes O(N * M) time in the worst case when all cells are 'O'.
# n = number of rows
# m = number of columns
# Space Complexity: O(N * M) in the worst case for the queue used in BFS

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # for this one basically go ahead and find all the O at the edges, do a traversal and find all the regions that are connected keep them as O#. go ahead and convert eveythign else as X 
        # now convert O# back to O 
        n = len(board)
        m = len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def findConnected(i, j): 
            q = deque()
            q.append((i, j))
            board[i][j] = "O#"

            while q:
                r, c = q.popleft()

                for dr, dc in directions: 
                    nr = r + dr
                    nc = c + dc 

                    if nr in range(n) and nc in range(m) and board[nr][nc] == "O":
                        q.append((nr, nc))
                        board[nr][nc] = "O#"


        
        #checking upper and lower rows
        for j in range(m):
            if board[0][j] == "O":
                findConnected(0, j)
            if board[n-1][j] == "O":
                findConnected(n-1, j)

        #checking for side col 0 and last col
        for i in range(n):
            if board[i][0] == "O":
                findConnected(i, 0)
            if board[i][m-1] == "O":
                findConnected(i, m -1)


        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O#":
                    board[i][j] = "O"        
