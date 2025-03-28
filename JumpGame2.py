# Leetcode Link: https://leetcode.com/problems/jump-game-ii/description/
# Category: Arrays and BFS(optional) and Queue(optional)

class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        Since we need to find the minimu steps, think of it as a graph and BFS
        take your starting point in the graph as index 0
        where can you go from here? the number of jumps you can take are your neighbours 
        Solved!
        T.C: O(n)
        S.C: O(n) - visited set and queue
        '''
        jumps = 0 
        q = deque()
        q.append(0)
        n = len(nums)
        visited = set()
        visited.add(0)

        while q:
            nq = len(q)
            for i in range(nq):
                element = q.popleft()
                if element == n - 1:
                    return jumps
                for nextelement in range(1, nums[element] + 1):
                    if element + nextelement not in visited:
                        q.append(element + nextelement)
                        visited.add(element + nextelement)
            jumps += 1
        return jumps 
