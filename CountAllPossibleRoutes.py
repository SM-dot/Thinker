# LeetCode Problem Link: https://leetcode.com/problems/count-all-possible-routes/
# LeetCode Problem: 1575. Count All Possible Routes
# Category: Dynamic Programming, Depth-First Search, Graph


from collections import deque 
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        '''
        Seems to be a bfs here 
        In our q, u go ahead and add the starting point, then u see where else can u go from there:
        instead of adj list u have a range 0 to n
        skip j == i 
        check if fuel = fuel - (abs(locations[i] - locations[j])) satisifes if yes add it to the q 
        if not ignore it 
        if your current location == target u add +1 to the answer 
        also in the priority q keep the node and the fuel left to satudy the conditions

        Concerns as of now: no visited set, hoping ends when pq ends does not seem like the best strat tho. Let's code adnd see :) 

        BFS would fail here in case of memory cause note that the question is not asking is there a short path it is asking to count a path SO THINK DFS!!!! You meesed up here


        This problem is actually a simple recurision prolem with a DP.

        Just follow as the question says 

        def dfs(start, finish, fuel):
            if your feule is less then u cannot go here return 0 

            if your satrt == finishe then note that this is a possible answer 
            Howerever, u still have node i to j to figure out from. Go ahead and figure thsoe out as well. 

            this will pass the base cases but after that need to do DP, what is changing in this? In this question the only thing that is chaging is the start node and the fuel amount so u have a 2D dp. 

            Time Complexity: 
            What about time ciomplexity note that ur DP is n * fuel and u will also be going over n node, technically n -1 for each node cause i != j then go ahead and multiply that so u end up getting n * n * fuel. 

            Space complexity: O(n*fuel) for the dp table and O(fuel) for the recursive stack, in the worst case when the recursion goes as deep as the fuel amount. However, since
            O(n*fuel) the dp tabel dominates over the recurisve stack 

            Now let's code!!! 
        '''
        n = len(locations)
        dp = [[-1 for i in range(201)] for j in range(101)]
        mod = 10**9 + 7 
        def dfs(start, fuel):
            nonlocal n 
            if fuel < 0:
                return 0
            
            if dp[start][fuel] != -1:
                return dp[start][fuel]

            ans = 0 
            if start == finish:
                ans += 1
                # do not return here cause u also need find all other i's for it 

            for i in range(n):
                if start != i:
                    remainingFuel = fuel - abs(locations[start] - locations[i])
                    ans += dfs(i, remainingFuel)
            dp[start][fuel] = ans
            return dp[start][fuel]
        
        

        return dfs(start, fuel) % mod 