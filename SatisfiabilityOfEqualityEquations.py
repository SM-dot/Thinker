# Leetcode Link: https://leetcode.com/problems/satisfiability-of-equality-equations/
# Category: Graphs, Optional DSU 
'''
Basically in this question we can use DSUs to group equation variables. If we just use a regular hashmap it can be a bit messy as we would need to identify all paths. 
DSU is a cleaner solution. 
Basically when you process all == first you are putting them in a set 
Then when you go to process != and find that the 2 varibles are already in the same set it means that there is a conflict this not possible. 
Problem solved! Now let's code

Note: Here I am using a rank and path compressed DSU 
'''
class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, i):
        if self.parent[i] == i:
            return i 
        
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)

        if (self.rank[x_parent] > self.rank[y_parent]):
            self.parent[y_parent] = x_parent
        
        elif (self.rank[y_parent] > self.rank[x_parent]):
            self.parent[x_parent] = y_parent
        
        else:
            self.parent[x_parent] = y_parent
            self.rank[y_parent] += 1
        
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        dsu = DSU(26) # as only lower case letters possible 

        # first process all ==
        for eq in equations: 
            if eq[1] == "=":
                u = ord(eq[0]) - ord('a')
                v = ord(eq[3]) - ord('a')
                dsu.union(u, v)
        
        # now process all !='s 
        for eq in equations:
            if eq[1] == "!":
                u = ord(eq[0]) - ord('a')
                v = ord(eq[3]) - ord('a')
                u_parent = dsu.find(u)
                v_parent = dsu.find(v)
                if u_parent == v_parent:
                    return False 
        return True 


        
