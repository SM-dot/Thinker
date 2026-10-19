class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        '''
        This is actually a cute brain exercise to solve. 

        So the key thing to undertand here is that we need to return the max sum and not the value we are assigning to the node. So if we get the frequency and then multiply that with the highest value, anf then the second most frequent one with the nexy hgihest value and so on and so forth. If we take a greedy approach we can then solve it. 

        O(n) time too. Very straightforward
        '''
        degrees = [0] * n

        for u, v in roads:
            degrees[u] += 1
            degrees[v] += 1
        
        degrees.sort()
        total = 0
        value = 1 

        for i in range(n):
            total += value * degrees[i]
            value += 1

        return total 
