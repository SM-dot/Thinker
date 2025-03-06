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
