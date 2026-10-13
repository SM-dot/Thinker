# Leetcode: Earliest Moment When Everyone Become Friends
# Problem Link: https://leetcode.com/problems/earliest-moment-when-everyone
# free acces: https://jamesperalta.com/code-editor/practice/1101?origin=peralta75&returnTo=%2Fperalta75&returnLabel=Back+to+Peralta+75
# time complexity: O(N log N) where N is the number of logs
# space complexity: O(N) where N is the number of logs


class DSU: 
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.components = n
        self.size = [1] * n 
    
    def find(self, x):
        if self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent == y_parent:
            return 
        
        if self.size[x_parent] < self.size[y_parent]:
            self.parents[x_parent] = y_parent
            self.size[y_parent] += self.size[x_parent]
        else:
            self.parents[y_parent] = x_parent
            self.size[x_parent] += self.size[y_parent]

        self.components -= 1



def earliest_acq(logs: list[list[int]], n: int) -> int:
    # Write your solution here
    '''
    This is what I am thinking: 
        1. sort the input based on times
        2. union the friends 
        3. keep track of components, if components == 1, return the time that happens
    time complexity: O(N log N) where N is the number of logs
    space complexity: O(N) where N is the number of logs

    time complexity breakdown:
    1. sorting the logs takes O(N log N)
    2. union and find operations take O(log N) on average, so for N logs, it takes O(N log N)
    3. overall time complexity is O(N log N)
    space complexity breakdown:
    1. DSU data structure takes O(N) space for parents and size arrays  
    '''
    dsu = DSU(n)
    logs.sort(key = lambda arr : arr[0])

    for time, f1, f2 in logs:
        dsu.union(f1, f2)
        if dsu.components == 1:
            return time 
    return -1