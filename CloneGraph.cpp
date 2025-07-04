// Leetcode Link: https://leetcode.com/problems/clone-graph/description/
// Problem Number: 133
// Category: Graph Traversal and Maps 

// BFS
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
    Node* cloneGraph(Node* node) {
        /*
        For this question, it is first evry important to understand what a deep copy means. 
        Deep Copy -> the new nodes that you will create need to be stored at a new location which means that a new object must be created for the nodes. For example you can have 2 nodes with the same value and neighbours. However in order for them to be deep copies of each other they must hold 2 different addresses in the memory. 
        If both of them are in the same address then it is not considered a deep copy. 

        Now, what do you need to create a deep copy? The original node, and to keep track if you have already created a deep copy or not. 
        Why do you need the original node? This will tell you the neighbours that your deep copy should have 
        Why do you need to keep track if you have created a deep copy before or not? This is because in a graph you can reach a node from multiple paths, if you keep on creating a new deep copy the graph will actually never connect correctly. 
        This indicates that we need a data structure to store these, thus maps is perfect! 
        Map<Node*, Node*> => Old Node or Original Node, New Node

        In order to create a deep copy you need to visit each node of the original graph, thus you also need to have a traversal algorithm. You can use DFS or BFS. 

        Time Complexity: O(n) -> traversal time
        Space Complexity: O(n) -> for each node, creating a new node and storing in a map

        The below solution uses BFS, let's start coding!
        */
        
        if (node == NULL)
            return NULL;

        Node* newNode = new Node(node->val);
        unordered_map<Node*, Node*> mp;
        queue<Node*> q;
        q.push(node);
        mp[node] = newNode;

        while(!q.empty())
        {
            Node* element = q.front();
            q.pop();
            Node* copiedNode = mp[element];

            for(Node* ngbr: element->neighbors)
            {
                if (mp.find(ngbr) == mp.end())
                {
                    Node* ngbrCopy = new Node(ngbr->val);
                    mp[ngbr] = ngbrCopy;
                    copiedNode->neighbors.push_back(mp[ngbr]);
                    q.push(ngbr);
                }
                else
                {
                    copiedNode->neighbors.push_back(mp[ngbr]);
                }
            }

        }

        return mp[node];
    }
};

//DFS:

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
// fun version control

// RV July 3rd 2025
