# Leetcode Link: https://leetcode.com/problems/similar-string-groups/
# Category: DFS, BFS, Union Find(otpional but beautiful)

class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0] * n
    
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
        
        if self.rank[y_parent] > self.rank[x_parent]:
            self.parents[x_parent] = y_parent
        elif self.rank[x_parent] > self.rank[y_parent]:
            self.parents[y_parent] = x_parent
        else: 
            self.parents[y_parent] = x_parent
            self.rank[x_parent] += 1
class Solution:
    def isSimilar(self, s1, s2):
        n = len(s1)
        diff = 0
        for i in range(n):
            if s1[i] != s2[i]:
                diff += 1
        return diff == 0 or diff == 2

    def numSimilarGroups(self, strs: List[str]) -> int:
        '''
        Break this question in 2 parts: 
        1. Finding if 2 words are similar 
        2. Finding the groups 

        1. Finding if 2 words are similar 
        given in the question: either identical or can swap any 2 characters 
        iterate through the length of the words and calculate any place where the characters of the string don't match - store it in a variable called diff. If diff == 2 or dif == 0 implies that letters can be swapped and these 2 can be grouped. 

        2. Union
        This question can also be solved with dfs and bfs but Union seems to be a bit more intuitive here. Ok, so now you go ahead and keep i and j pointers, nested loop. whenever 2 words are similar union them. 
        We have usually seen integers in DSU, so you will union the index of the word. Once done, iterate over all the indexes and keep track of the number of unique parents. Return the unique parents as that is the number of components. 

    Time Complexity:
        - O(N² * L), where N is the number of words and L is the word length (for similarity check).
        - DSU operations are amortized nearly constant (O(α(N))).
    Now, let's code!
        '''
        n = len(strs)
        dsu = DSU(n)

        for i in range(n):
            for j in range(i + 1, n):
                if self.isSimilar(strs[i], strs[j]):
                    dsu.union(i, j)
        
        number_of_parents = set()
        for i in range(n):
            parent = dsu.find(i)
            if parent not in number_of_parents: 
                number_of_parents.add(parent)
        
        return len(number_of_parents)

