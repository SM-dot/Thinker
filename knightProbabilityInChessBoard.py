# LeetCode Problem Link: https://leetcode.com/problems/knight-probability-in-chessboard/
# LeetCode Problem: 688. Knight Probability in Chessboard
# Category: Dynamic Programming, Recursion
# Difficulty: Medium

'''
Simple recursion solution
Time complexity: O(8^k) where k is the number of moves. This is because in the worst case, the knight can move to 8 different positions at each step, leading to a branching factor of 8.
Space complexity: O(k) due to the recursive call stack, where k is the number of
moves. In the worst case, the recursion can go as deep as k levels.
'''
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [[2, -1], [2, 1], [-2, -1], [-2, 1], [1, 2], [-1, 2], [1, -2], [-1, -2]]
        
        def solve(i, j, k):
            if i not in range(n) or j not in range(n):
                return 0
            
            if k == 0:
                return 1 
            
            answer = 0

            for dr, dc in directions:
                nr = dr + i
                nc = dc + j

                answer += solve(nr, nc, k - 1)
            
            return answer / 8
        
        return solve(row, column, k)
            

'''
Basic 3 dimensional array memoization solution 
time complexity: O(n^2 * k) where n is the size of the chessboard and k is the number of moves. This is because we are filling a 3D dp array of size n x n x (k + 1).
Space complexity: O(n^2 * k) for the dp array, which stores the probability
of the knight being on each square of the chessboard after a certain number of moves.
'''
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [[2, -1], [2, 1], [-2, -1], [-2, 1], [1, 2], [-1, 2], [1, -2], [-1, -2]]
        dp = [[[-1 for _ in range(101)] for _ in range(n)] for _ in range(n)]
        
        def solve(i, j, k):
            if i not in range(n) or j not in range(n):
                return 0
            
            if k == 0:
                return 1 
            
            if dp[i][j][k] != -1:
                return dp[i][j][k]
            
            answer = 0

            for dr, dc in directions:
                nr = dr + i
                nc = dc + j

                answer += solve(nr, nc, k - 1)
            
            dp[i][j][k] = answer / 8
            return dp[i][j][k]
        
        return solve(row, column, k)


'''
New technique for memoising using a hashmap instead of a three dimensional array. 
Time complexity: O(n^2 * k) where n is the size of the chessboard and k is the number of moves. This is because we are filling a dp hashmap with entries for each square of the chessboard and each number of moves.
Space complexity: O(n^2 * k) for the dp hashmap, which stores the probability of the knight being on each square of the chessboard after a certain number of moves. In the
The time complexity is the same as the 3D array memoization solution, but the space complexity can be more efficient in practice, as we only store entries for the states that are actually computed during the recursion, rather than pre-allocating a large 3D array.
We are essentially jsut keeping track of visited states so in some scenrious it can be better 
the worse case is still the same. 
'''
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [[2, -1], [2, 1], [-2, -1], [-2, 1], [1, 2], [-1, 2], [1, -2], [-1, -2]]
        dp = [[[-1 for _ in range(101)] for _ in range(n)] for _ in range(n)]
        map_dp = {}
        
        def solve(i, j, k):
            if i not in range(n) or j not in range(n):
                return 0
            
            if k == 0:
                return 1 
            
            key = str(i) + "_" + str(j) + "_" + str(k)
            if key in map_dp:
                return map_dp[key]
            
            
            answer = 0

            for dr, dc in directions:
                nr = dr + i
                nc = dc + j

                answer += solve(nr, nc, k - 1)
            
            map_dp[key] = answer / 8
            return map_dp[key]
        
        return solve(row, column, k)
            