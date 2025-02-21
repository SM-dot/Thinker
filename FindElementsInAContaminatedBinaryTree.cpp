// Leetcode Porblem Link: https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/description
// Problem Number: 1261
// This can be solved using DFS or BFS both 
// Time complexity: O(n) where n is the number of nodes and this is due to the traversal of the tree
// In order to avoid a time complexity of O(n) when finding an element, we are using a set which takes an extra space, thus the space complexity is O(N)

// DFS
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class FindElements {
public:
    unordered_set<int> st;

    void dfs(TreeNode* root, int x)
    {
        if (root == nullptr)
            return; 
        
        root->val = x;
        st.insert(x);
        dfs(root->left, 2 * x + 1);
        dfs(root-> right, 2 * x + 2);
    }
    FindElements(TreeNode* root) {
        dfs(root, 0);
    }
    
    bool find(int target) {
        return st.count(target);
    }
};

// BFS
class FindElements {
public:
    unordered_set<int> st;

    void bfs(TreeNode* root, int x)
    {
        queue<TreeNode* > q;
        root->val = x;
        q.push(root);

        while(!q.empty())
        {
            TreeNode* element = q.front();
            q.pop();
            st.insert(element->val);

            if (element->left)
            {
                element->left->val = 2 * element->val + 1;
                q.push(element->left);
            }

            if (element->right)
            {
                element->right->val = 2 * element->val + 2;
                q.push(element->right);
            }
        }
    }

    FindElements(TreeNode* root) {
        bfs(root, 0);
    }
    
    bool find(int target) {
        return st.count(target);
    }
};
