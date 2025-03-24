// Available on Neetcode.io for free :) 
// Leetcode Link: https://leetcode.com/problems/alien-dictionary/
// Category: Grpahs, specifically - Topological Sort 
class Solution {
public:

    vector<int> toposort(vector<vector<int>>& adj)
    {
        int num_nodes = adj.size();
        vector<int> indegrees(num_nodes, 0); 
        queue<int> q;
        vector<int> result;
        int count = 0; 

        // calculating the indegrees
        for(int i = 0; i < num_nodes; i++)
        {
            auto u = adj[i];
            for(auto v : u)
            {
                indegrees[v] += 1;
            }
        }


        // finding all the elements with an indegree of 0 and putting them in the queue 
        for(int i = 0; i < num_nodes; i++)
        {
            if (indegrees[i] == 0)
                q.push(i);
        }

        while(!q.empty())
        {
            int element = q.front();
            q.pop();
            result.push_back(element);
            count += 1; 

            for(auto v: adj[element])
            {
                indegrees[v] -= 1;

                if (indegrees[v] == 0)
                    q.push(v);
            }

        }
        if (count == num_nodes) 
            return result; 
        else 
            return {}; 
    }

    string foreignDictionary(vector<string>& words) {
        // first create an adjacency list 
        // create it by finding all the a->b relations
        // then run toposort on it and return the result of toposort

        vector<vector<int>> adj(26);
        int n = words.size();

        for(int i = 0; i < n - 1; i++)
        {
            string word1 = words[i];
            string word2 = words[i + 1];

            if (word1.size() > word2.size() && word1.substr(0, word2.size()) == word2) 
            return "";
        
            int len = min(word1.size(), word2.size());

            for(int j = 0; j < len; j++)
            {
                if (word1[j] != word2[j])
                {
                    adj[word1[j] - 'a'].push_back(word2[j] - 'a');
                    break;
                }
            }
        }


        vector<int> topo_order = toposort(adj);
        if (topo_order.empty())
            return "";

        // convert vector int to a string 
        string ans = "";
        for(auto ch : topo_order)
        {
            ans += char(ch + 'a');
        }

        return ans; 
    }
};
