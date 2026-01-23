# LeetCode Problem: 2502. Design Memory Allocator
# LeetCode Link: https://leetcode.com/problems/design-memory-allocator/
# Category: Design, Array, Simulation
# Difficulty: Medium

# Explanation:
# To design a memory allocator, we can use a list to represent the memory blocks. Each
# index in the list corresponds to a memory unit, and the value at that index indicates
# whether the unit is free (0) or allocated to a specific mID. The allocate method searches
# for a contiguous block of free memory units of the requested size and assigns them to
# the given mID. The freeMemory method iterates through the memory list and frees all
# units associated with the specified mID, returning the count of freed units.  
# Time Complexity:
# - allocate: O(n) in the worst case, where n is the size of the memory, as we may need to scan the entire list.
# - freeMemory: O(n) in the worst case, as we may need to scan the entire list.
# Space Complexity: O(n) for storing the memory list.   
# Oprimised version could use maps - Need to think. more on this later. 
class Allocator:

    def __init__(self, n: int):
        self.mem = [0] * n 

    def allocate(self, size: int, mID: int) -> int:
        count = 0
        start = 0
        n = len(self.mem)

        if size > n:
            return -1 

        for i in range(n):
            if self.mem[i] == 0:
                if count == 0:
                    start = i
                count += 1
            
                if count == size:
                    for j in range(start, start + size):
                        self.mem[j] = mID
                    return start
            
            else:
                count = 0
        return -1
        

        

    def freeMemory(self, mID: int) -> int:
        freed = 0
        for i, id_ in enumerate(self.mem):
            if id_ == mID:
                self.mem[i] = 0
                freed += 1
        return freed 
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)