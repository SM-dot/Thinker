# LeetCode Problem: Number of Nodes in Subtree with Same Label
# Problem Link: https://leetcode.com/problems/number-of-nodes-in-subtree-with-the-same-label/
# Category: Tree, DFS

class Solution:
    '''
    Input: Number of nodes n, edges representing the tree, and a string labels where labels[i] is the label of the i-th node
    Operations:
    - Build an adjacency list to represent the tree
    - Use DFS to traverse the tree and count the number of nodes in each subtree with the same label
    - For each node, maintain a count of labels in its subtree and return the count for each node
    Output: List of counts where the i-th element is the number of nodes in the subtree rooted at node i with the same label as node i
    T.C: O(N) where N is the number of nodes in the tree
    S.C: O(N) for the adjacency list and recursion stack
    Using DFS to traverse the tree and count labels in the subtree
    '''
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        count = [0] * 26
        adj = defaultdict(list)
        answer = [0] * n 

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, parent):
            currentLabelValue = count[ord(labels[node]) - ord('a')]
            count[ord(labels[node])- ord('a')] += 1

            for child in adj[node]:
                if child != parent:
                    dfs(child, node)
            
            answer[node] =  count[ord(labels[node])- ord('a')] - currentLabelValue
            return 
        
        dfs(0, -1)
        return answer 
    



