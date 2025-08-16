# Leetcode 1146. Snapshot Array
# Problem Link: https://leetcode.com/problems/snapshot-array/
# Category: Array, Binary Search, Design


class SnapshotArray:
    def __init__(self, length: int):
        '''
        Brute force idea:
        would be to use a hashampa and store the array at each snapId
        However, that is an inefficient use of memory as we are only updating 1 index position while setting, the rest of the array remains the same. 

        So let's create a custom data structure 
        index -> [list -(snapId, val)]
        T.C: O(1) for set and snap
        T.C: O(logS) for get - S is the number of snaps taken at that index
        S.C: O(N + S) where N is the length of the array
        '''
        self.indexData = defaultdict(list)
        self.snapIndex = 0
        self.length = length
        # snapId, val
        for i in range(self.length):
            self.indexData[i].append((0, 0))
        

    def set(self, index: int, val: int) -> None:
        self.indexData[index].append((self.snapIndex, val))
        

    def snap(self) -> int:
        self.snapIndex += 1
        return self.snapIndex - 1
        

    def get(self, index: int, snap_id: int) -> int:
        # we want to get the last occurence of the snapId that we are searching for 
        # self.indexData[index] == [(0, 0), (0, 2), (0, 3), (0, 4), (1, 4), (1, 5), (1, 6)]
        # and snapId = 0, we want the last occurence of 0 which is (0, 4) instead of looking for this linearly we can quickly write a binary search algorithm and implement it. 
        l = 0
        r = len(self.indexData[index]) - 1
        data = self.indexData[index]
        result = 0 # this will hold 0, 3, and eventually what we are looking for which is 4

        while (l <= r):
            mid = l + (r - l) // 2
            if data[mid][0] <= snap_id:
                result = data[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return result 
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)