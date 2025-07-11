# LeetCode 1420. Build Array Where You Can Find The Maximum Exactly K Comparisons
# Problem Link: https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/
# Category: Dynamic Programming, Recursion, Memoization

# Recursive Solution
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        '''
        Basically need to find arrays that satisfy the condition

        m possibilities  _ _ for each index
        build tree for each possibility and in the check once reached the last index see if it matches the k constraint. If yes, add to result else move on

        Recursion Solution
        T.C: O(N^M)
        '''
        mod = 10^9 + 7
        def solve(index, searchCost, prevNumber):
            if index >= n:
                if searchCost == k:
                    return 1
                else:
                    return 0
            
            result = 0
            # for each index checking all m possinilities that can be filled 
            for i in range(m):
                if i > prevNumber: 
                    result = (result + solve(index + 1, searchCost + 1, i)) % mod
                else:
                    result = (result + solve(index + 1, searchCost, prevNumber)) % mod
            
            return result % mod
        
        return solve(0, 0, -1)
    

# Recursive + Memoization Solution
# T.C: O(n⋅k⋅m^2)
# S.C: O(n⋅k⋅m) + O(n) recursion stack
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        '''
        Recursion + Memoisation Solution
        T.C: O(n⋅k⋅m^2)
        '''
        mod = 10**9 + 7
        t = [[[-1 for _ in range(m)] for _ in range(n )] for _ in range(n)]

        def solve(index, searchCost, prevNumber):
            if index >= n:
                if searchCost == k:
                    return 1
                else:
                    return 0
            
            if t[index][searchCost][prevNumber] != -1:
                return t[index][searchCost][prevNumber]

            result = 0
            # for each index checking all m possinilities that can be filled 
            for i in range(m):
                if i > prevNumber: 
                    result = (result + solve(index + 1, searchCost + 1, i)) % mod
                else:
                    result = (result + solve(index + 1, searchCost, prevNumber)) % mod
            
            t[index][searchCost][prevNumber] =  result % mod
            return t[index][searchCost][prevNumber]
        
        return solve(0, 0, -1)