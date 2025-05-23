# Leetcode Link: https://leetcode.com/problems/sum-of-distances-in-tree/
# Category: Trees, Graphs, DFS, Recursion (low level concept)

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        Ok brute force approach was that from each node we do a DFS/BFS and get the total depth of the tree. This approach took O(n*n) time. 
        Now, here is an optimal approach. 

        Let's say you know the asnwer for the parent node, let's say it is 0. You know that the sum of depth for 0 is 8. so for its child, when that becomes the node u want to calculate for you will notice that all the nodes below the child are reducing their distance or depth by 1 compared to 0th parent node. see 2->3 = 1, 2->4 = 1, but 0->3=2, 0->4=2. Similarly 0->1=1 but 2->1=2 so above the child 2 all nodes did +1 to the parent 0 distance. 

        From these observations you can come up with a formula: 
        child answer = parent answer -(no of nodes below the child and including the child cause 2->2=0 but 0->2=1) + (total nodes - no of nodes below the child and inclusing the child = no of nodes above the child + because remember 0->1=1 but 2->1 = 2)

        Ok now let's see the code story:
        You will need the first DFS to go ahead and calculate the answer for the 0th node and also calculate for each node the number of nodes below it. 

        Then you will need another DFS to calculate the result based on our formula 

        Time complexity: O(n+n) = O(2n) = O(n)
        '''

        result = [0] * n
        count = [1] * n 
        adj = defaultdict(list)
        self.rootAnswer = 0
        
        for edge in edges:
            u = edge[0]
            v = edge[1]
            adj[u].append(v)
            adj[v].append(u)
        
        def dfsRoot(node, parent, depth):
            number_of_nodes = 1
            for child in adj[node]:
                if child != parent: 
                    number_of_nodes += dfsRoot(child, node, depth + 1)
                    self.rootAnswer += depth + 1
            count[node] = number_of_nodes
            return number_of_nodes # dont forget as crucial for answer calculation in the dfs block above 
        def dfsAll(node, parent, answer_p):
            result[node] = answer_p
            for child in adj[node]:
                if child != parent: 
                    dfsAll(child, node, answer_p + (n-count[child]) - count[child])
        
        dfsRoot(0, -1, 0)
        dfsAll(0, -1, self.rootAnswer)
        return result
