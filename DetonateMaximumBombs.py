# Leetcode link: https://leetcode.com/problems/detonate-the-maximum-bombs/
# Category: Graphs 
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        '''
        Intutively, we can see that this is leaning towards a BFS/DFS traversal. BFS is probably more intuitive as it is simlar to the rotten orange problem, where you keep on rotting fresh oranges around you. Similiarly if something is in range of the bomb here you can go ahead and detonate it. 

        The main question is, how do you know if something is in range of the bomb? This is more math and gemoetry. In geometry you can find the diatnce between 2 points, the 2 points can be the centre of the circles. Formula: 
        sqrt((x2-x1)**2 + (y2-y1)**2) = d
        if the radius of the circle you are currently at is greater than equal to d(distance between the 2 circles) it means that you can detonate it. Directional graph here, cause it is possible that from circle 1 you can detonate circle 2 but from circle 2 you cannot detonate one. This is just geometry. 

        Now moving to the algorithm. First vuild your adjaceny list, then for each bomb call dfs or bfs. Return the max count. During dfs or bfs count how many nodes were visited. Done! 

        Now, let's code :)
        '''
        n = len(bombs)
        adj = collections.defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                d = sqrt((x2 - x1)**2 + (y2 - y1)**2)

                if d <= r1:
                    adj[i].append(j)
                
                if d <= r2: 
                    adj[j].append(i)
        
        def dfs(i, visit):
            if i in visit: 
                return 0
            res = 1
            visit.add(i)
            for nextBomb in adj[i]:
                res += dfs(nextBomb, visit)
            return res 
        
        res = 0
        for i in range(n):
            res = max(res, dfs(i, set()))
        
        return res


# BFS Code: 
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        res = 0

        def bfs(i):
            q = deque()
            q.append(i)
            visited = set()
            visited.add(i)
            count = 0

            while q:
                bomb = q.popleft()
                count += 1
                x1, y1, r1 = bombs[bomb]

                for index, bomb in enumerate(bombs):
                    if index not in visited: 
                        x2, y2, r2 = bomb
                        d = sqrt((x2 - x1)**2 + (y2 - y1)**2)
                        if d <= r1:
                            q.append(index)
                            visited.add(index)
            return count 




        for i in range(n):
            res = max(res, bfs(i))
        return res 
