# 380. Insert Delete GetRandom O(1)
# Problem Link: https://leetcode.com/problems/insert-delete-getrandom-o1/
# Category: Design, Hash Table, Randomized
from collections import defaultdict
import random

class RandomizedSet:
    '''
    Let's say we use an array. 
    In an array/ list inserting is O(1) time as you insert it at the back. 
    Getting random is also O(1) because you generate a random index and return the element at that index, since lookup in lists in python is also O(1) this operation is also O(1)
    However, for removing - you need to find the index in which the element is and then also move other indexes to fill that gap which is O(n+n) - fidning index and moving other elements

    Solution for removing - in addition to the array store a hashmap that has the value mapped to the index. 
    lets say you have the element to remove at index i, swap it with the last element in the list. Then pop the last element from the list and update the map accordingly - all this will be done in O(1)

    Now lets code! 
    # Time Complexity: O(1) for all operations
    # Space Complexity: O(n) for storing elements in map and list
    '''

    def __init__(self):
        self.map = defaultdict(int)
        self.lst = []
        

    def insert(self, val: int) -> bool:
        if val not in self.lst:
            self.lst.append(val)
            self.map[val] = len(self.lst) - 1
            return True
        return False

        

    def remove(self, val: int) -> bool:
        if val not in self.lst:
            return False 
        
        index = self.map[val]
        lastelement = self.lst[len(self.lst) - 1]
        self.lst[index] = lastelement
        self.lst.pop() # O(1)

        self.map[lastelement] = index
        del self.map[val]
        return True 
        

    def getRandom(self) -> int:
        random_index  = random.randint(0, len(self.lst) - 1)
        return self.lst[random_index]
        

instance = RandomizedSet()
print(instance.insert(1))
print(instance.remove(2))
print(instance.insert(2))
print(instance.getRandom())
print(instance.remove(1))
print(instance.insert(2))
print(instance.getRandom())

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()