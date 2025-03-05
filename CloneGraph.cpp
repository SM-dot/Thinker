// Leetcode Link: https://leetcode.com/problems/clone-graph/description/
// Problem Number: 133
// Category: Graph Traversal and Maps 

//DFS:
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    //          <OG Node, cloned Node>
    unordered_map<Node*, Node*> mp;

    void DFS(Node* node, Node* newNode)
    {
        for(Node* n: node->neighbors)
        {
            // this means that we have not created a deep copy yet
            if (mp.find(n) == mp.end())
            {
                Node* ngbrCopy = new Node(n->val);
                mp[n] = ngbrCopy;
                newNode->neighbors.push_back(mp[n]);
                DFS(n, ngbrCopy);
            }
            else
            {
                newNode->neighbors.push_back(mp[n]);
            }
        }
    }

    Node* cloneGraph(Node* node) {
        if (node == NULL)
            return NULL; 
        Node* newNode = new Node(node->val);
        mp[node] = newNode;
        DFS(node, newNode);
        return mp[node]; // can also say return newNode here as the DFS will handle the rest and we just need to return the head that was given in the function
    }
};
