// Leetcode Link: https://leetcode.com/problems/most-profitable-path-in-a-tree/description/?envType=daily-question&envId=2025-02-24
// Problem Number: 2467

// DFS 
class Solution {
public:
    unordered_map<int, vector<int>> adj;
    int maxIncome; 

    bool BobDFS(int currNode, int time, vector<bool>& visited, unordered_map<int, int>& BobMap)
    {
        visited[currNode] = true; 
        BobMap[currNode] = time; 

        if (currNode == 0)
            return true;

        for(auto& ngbr: adj[currNode])
        {
            if (visited[ngbr] == false && BobDFS(ngbr, time + 1, visited, BobMap) == true)
                return true; 
        }

        // if the path did not lead to 0 then remove it from the map
        BobMap.erase(currNode);
        return false;
    }

    void AliceDFS(int currNode, int time, int income, vector<bool>& visited, vector<int>& amount, unordered_map<int, int>& BobMap)
    {
        visited[currNode] = true; 

        if (BobMap.find(currNode) == BobMap.end() || time < BobMap[currNode])
            income += amount[currNode];
        
        else if (BobMap[currNode] == time)
            income += (amount[currNode] / 2);
        
        // if leaf node and to avoid error make sure the starting node is not the leaf node
        if (adj[currNode].size() == 1 && currNode != 0)
            maxIncome = max(maxIncome, income);

        for(auto& ngbr: adj[currNode])
        {
            if (visited[ngbr] == false)
                AliceDFS(ngbr, time + 1, income, visited, amount, BobMap);
        }
        
    }
    int mostProfitablePath(vector<vector<int>>& edges, int bob, vector<int>& amount) {
        // do a dfs for bob's journey
        // in a map store the node and time at which bob visits the node 

        // Now go ahead and do a dfs/bfs for Alice
        // When you do a traversal for Alice, multiple things need to be noted
        // 1. If Bob has already visited a node, add 0 to the income 
        // 2. If Alice is visiting a node first => Alice time < Bob's time to reach node x, add that to the income 
        // 3. If Alice time == Bob time for node x then add amount/2 to the income as mentioned in the question. 
        // 4. Compare the income to the maxincome variable as we want the max income possible
        // Let's code! 

        // Firstly, building an adjacency list
        for(auto& edge: edges)
        {
            int a = edge[0];
            int b = edge[1];

            adj[a].push_back(b);
            adj[b].push_back(a);
        }

        int n = amount.size(); // this gives us the number of nodes

        //Bob's DFS
        vector<bool> visited(n, false);
        //            node, time
        unordered_map<int, int> BobMap;
        //start node, time, visited, map to fill
        BobDFS(bob, 0, visited, BobMap);



        // Alice's DFS
        maxIncome = INT_MIN;
        int income = 0;
        visited.assign(n, false);
        //start node, time, income, visited
        AliceDFS(0, 0, income, visited, amount, BobMap);

        return maxIncome; 

    }
};
