# Leetcode 1061. Lexicographically Smallest Equivalent String
# Problem Link: https://leetcode.com/problems/lexicographically-smallest-equivalent-string/
# Category: Union Find

'''
Input: Two strings s1 and s2 representing pairs of equivalent characters, and a base string baseStr
Operations:
- Use Union-Find (Disjoint Set Union) to group equivalent characters together
- For each character in baseStr, find its representative character in the union-find structure
- Construct the result string by replacing each character in baseStr with its representative character
Output: The lexicographically smallest equivalent string formed by replacing characters in baseStr with their representatives
T.C: O(N + M) where N is the length of s1 and M is the length of baseStr
S.C: O(1) for the union-find structure since it only stores 26 characters (a-z)
Using Union-Find to group equivalent characters and find the lexicographically smallest equivalent string   
'''
class DSU: 
    def __init__(self, n):
        self.parents = [i for i in range(n + 1)]
        self.size = [1 for i in range(n + 1)]
    
    def find(self, x):
        if x == self.parents[x]:
            return x
        
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent == y_parent:
            return 
        
        # Union based on lexicographical order
        if x_parent < y_parent:
            self.parents[y_parent] = x_parent
            self.size[x_parent] += self.size[y_parent]
        else:
            self.parents[x_parent] = y_parent
            self.size[y_parent] += self.size[x_parent]

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dsu = DSU(26)
        n = min(len(s1), len(s2))

        for i in range(n):
            x = ord(s1[i]) - ord('a')
            y = ord(s2[i]) - ord('a')
            dsu.union(x, y)
        
        result = ""
        for letter in baseStr:
            parentVal = dsu.find(ord(letter) - ord('a'))
            parentLetter = chr(parentVal + ord('a'))
            result += parentLetter
        
        return result

