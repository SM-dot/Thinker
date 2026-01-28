# LeetCode Problem Link: https://leetcode.com/problems/find-the-town-judge/
# LeetCode Problem: 997. Find the Town Judge
# Category: Array, Graph
# Difficulty: Easy


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        '''
        think like this 
        indegrees = []
        outdegrees = []
        for whichever indegrees == n - 1 and outdegrees == 0
        thats the answer TC = O(N), SC = O(2N)

        approach 2:
        just count the indgrees
        initially everything 0
        if 1 -> 3
        implies that 1 canot be the answe so make it -1, just check whichever gets to n - 1 thats the answer and if tehre are 2 such people then no answer 
        TC = O(N)
        SC = O(N)       
         '''

        indegrees = [0] * (n + 1)

        for a, b in trust:
            indegrees[b] += 1
            indegrees[a] = -1

        for i in range(1, n + 1):
            if indegrees[i] == n - 1:
                return i
        return -1