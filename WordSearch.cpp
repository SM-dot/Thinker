/*
 * Leetcode: Word Search 
 * Link: https://leetcode.com/problems/word-search/
 * Approach:
 * This solution uses a **Backtracking + DFS (Depth-First Search)** approach to check 
 * if the given word exists in the 2D board by forming a contiguous sequence.
 * 
 * 1. Iterate through each cell in the board, searching for the first character of `word`.
 * 2. If a match is found, call the recursive `find()` function to explore all four possible 
 *    directions (right, left, up, down).
 * 3. The `find()` function:
 *    - Returns true if all characters in `word` are matched.
 *    - Stops searching if the indices go out of bounds, if the character does not match, 
 *      or if the cell is already visited.
 *    - Marks the current cell as visited (using '$') to avoid reuse in the same path.
 *    - Explores all four possible moves recursively.
 *    - Backtracks by restoring the original character after recursion.
 * 4. If any path successfully finds the word, return true; otherwise, return false.
 * 
 * Time Complexity: O(N * M * 4^L), where:
 *   - N, M = board dimensions
 *   - L = length of the word
 *   - Each cell has 4 possible directions to explore at each step.
 * 
 * Space Complexity: O(L) (recursive stack depth).
 */

class Solution {
public:
    int n; // Number of rows in the board
    int m; // Number of columns in the board

    // Directions array representing the 4 possible movements (right, left, up, down)
    vector<vector<int>> directions {
        {0, 1},  // Move right
        {0, -1}, // Move left
        {-1, 0}, // Move up
        {1, 0}   // Move down
    };

    // Helper function to check if the word can be formed starting from board[i][j]
    bool find(int i, int j, int idx, vector<vector<char>>& board, string& word)
    {
        // Base case: If the entire word has been matched, return true
        if (idx == word.length())
            return true;
        
        // Boundary check and visited cell check
        if (i >= n || j >= m || i < 0 || j < 0 || board[i][j] == '$')
            return false; 
        
        // If current character does not match the required character in word
        if (board[i][j] != word[idx])
            return false; 
        
        // Temporarily mark the cell as visited to avoid revisiting
        char temp = board[i][j];
        board[i][j] = '$';

        // Explore all four possible directions
        for(auto& dir: directions)
        {
            int new_i = i + dir[0];
            int new_j = j + dir[1];

            // Recursively search in the new direction
            if (find(new_i, new_j, idx + 1, board, word))
                return true;
        }

        // Backtrack: Restore the original character before returning
        board[i][j] = temp;
        return false; 
    }

    // Function to check if the word exists in the grid
    bool exist(vector<vector<char>>& board, string word) {
        n = board.size();      // Get the number of rows
        m = board[0].size();   // Get the number of columns

        // Iterate through every cell in the board
        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < m; j++)
            {
                // If the first character of the word matches board[i][j], start searching
                if (word[0] == board[i][j])
                {
                    // If the word is found starting from (i, j), return true
                    if (find(i, j, 0, board, word))
                        return true;
                }
            }
        }

        // If no match is found, return false
        return false; 
    }
};



# Python Code: 
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def search(i, j, index, visited):
            if index >= len(word):
                return True

            if i not in range(n) or j not in range(m) or (i, j) in visited or board[i][j] != word[index]:
                return False
            
            visited.add((i, j))

            for dx, dy in directions:
                r = dx + i
                c = dy + j 
                if search(r, c, index + 1, visited):
                    return True
            
            visited.remove((i, j))
            
            return False 

        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if search(i, j, 0, set()):
                        return True
        return False 

        
        