# Leetcode 36. Valid Sudoku
# Problem Link: https://leetcode.com/problems/valid-sudoku/
# Category: Array, Hash Table


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        tracker = defaultdict(set)

        n = len(board)
        m = len(board[0])

        for i in range(n):
            for j in range(m):
                row = i
                col = j
                val = board[i][j]
                if val != '.':
                    if val in tracker[("r", row)]:
                        # print("DEBUG: row fail ", i, " ", j)
                        return False
                    else:
                        tracker[("r", row)].add(val)              
                    if val in tracker[("c", col)]:
                        # print("DEBUG: col fail ", i, " ", j)
                        return False
                    else:
                        tracker[("c", col)].add(val)
                    if val in tracker[(row//3, col//3)]:
                        # print("DEBUG: box fail ", i, " ", j)
                        return False
                    else:
                        tracker[(row//3, col//3)].add(val)

        return True 