// Leetcode Link: https://leetcode.com/problems/pacific-atlantic-water-flow/description/
// Problem number: 417
// Category: Graph Traversals 
class Solution {
public:
    int n;
    int m;
    void dfs(int r, int c, set<pair<int, int>>& visited, int prevHeight, vector<vector<int>>& heights) {
        if (visited.find({r, c}) != visited.end() || r < 0 || c < 0 || r >= n || c >= m || heights[r][c] < prevHeight)
            return;

        visited.insert({r, c});
        dfs(r - 1, c, visited, heights[r][c], heights);
        dfs(r + 1, c, visited, heights[r][c], heights);
        dfs(r, c - 1, visited, heights[r][c], heights);
        dfs(r, c + 1, visited, heights[r][c], heights);
    }

    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        /*
        Brute force would be to chek from each cell if I can reach the atlantic and the pacific ocean. But the main issue here is that it will be redundant and very heavy in time complexity. 

        So what is a better approach? 

        We know that all the edges of the grid either touch the Pacific Ocean or the Atlantic Ocean. If we visit all cells from these we would have found cells that touch the pacific and the atlantic ocean. We have kind of reverse engineered the problem. 

    Time Complexity: 
    DFS Traversal: O(n × m)
    Set Insertions & Lookups: O(n × m log(n × m))
    Finding Common Cells: O(n × m log(n × m))



        Let's code!
        */

         vector<vector<int>> answer; 
        n = heights.size();
        m = heights[0].size();

        set<pair<int, int>> pacific; 
        set<pair<int, int>> atlantic;

        // DFS from top row (Pacific) and bottom row (Atlantic)
        for (int i = 0; i < m; i++) {
            dfs(0, i, pacific, heights[0][i], heights);
            dfs(n - 1, i, atlantic, heights[n - 1][i], heights);
        }

        // DFS from left column (Pacific) and right column (Atlantic)
        for (int i = 0; i < n; i++) {
            dfs(i, 0, pacific, heights[i][0], heights);
            dfs(i, m - 1, atlantic, heights[i][m - 1], heights);
        }

        // Collect all cells that can reach both oceans
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (pacific.find({i, j}) != pacific.end() && atlantic.find({i, j}) != atlantic.end())
                    answer.push_back({i, j});
            }
        }

        return answer;
    }
};


/*
Python Version: 
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # The brute force method that might come to mind is to check from each cell if it can reach the Pacific ocean or atlantic ocean. However, that is too time consuming as you would visit each cell, then do a dfs to find paicific, then atlantic. 
        # A more optimal solution by reverse engineering the approach is to start from the pacific ocean and atlantic ocean cells (we already know these as these are the borders). Do a traversal and store all the cells that can be reached from the atlantic and pacific ocean. 
        # In the end compare the cells that are in the atlantic and pacific bag 
        # Add those in the answer and return 

        pacific = set()
        atlantic = set()

        rows = len(heights)
        cols = len(heights[0])

        directions = [[-1, 0], [0, 1], [0, -1], [1, 0]]

        def dfs(i, j, visited):
            visited.add((i, j))

            for dir in directions:
                newr = i + dir[0]
                newc = j + dir[1]

                if (newr in range(rows) and newc in range(cols) and heights[newr][newc] >= heights[i][j] and (newr, newc) not in visited):
                    dfs(newr, newc, visited)

            
        # The top row for pacific and bottom for atlantic 
        for i in range(cols):
            dfs(0, i, pacific)
            dfs(rows - 1, i, atlantic)
        
        # The left side for pacific and the right side for atlantic
        for i in range(rows):
            dfs(i, 0, pacific)
            dfs(i, cols - 1, atlantic)
        
        return list(pacific & atlantic)
*/
