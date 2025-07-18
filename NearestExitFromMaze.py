# LeetCode 1926. Nearest Exit from Entrance in Maze
# Problem Link: https://leetcode.com/problems/nearest-exit-from-entrance-in-ma  
# Category: BFS, Graph

class Solution:
    '''
    Input: 2D grid with walls and paths, entrance coordinates
    Operations:
    - BFS from the entrance to find the nearest exit
    - An exit is any path cell on the border of the grid, excluding the entrance
    Output: Minimum number of steps to the nearest exit, -1 if no exit is reachable
    T.C: O(N * M) where N is number of rows and M is number of columns
    S.C: O(N * M) for the queue and visited set
    Can avoid the visited set by marking visited cells in the maze itself but that would modify the input
    which is not always desirable'''
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque()
        q.append(entrance)
        visited = set()
        steps = 0
        n = len(maze)
        m = len(maze[0])
        visited.add((entrance[0], entrance[1]))
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        
        while q:
            x = len(q)
            for _ in range(x):
                i, j = q.popleft()
                if (i == 0 or i == n - 1 or j == 0 or j == m - 1) and [i, j] != entrance:
                    return steps

                for dx, dy in directions:
                    row = dx + i
                    col = dy + j 
                    if row in range(n) and col in range(m) and maze[row][col] != '+' and (row, col) not in visited: 
                        visited.add((row, col))
                        q.append((row, col))
            steps += 1

        return -1 
                
            