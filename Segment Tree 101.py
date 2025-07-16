# LeetCode 303. Range Sum Query - Immutable
# Problem Link: https://leetcode.com/problems/range-sum-query-immutable/
# Category: Segment Trees, Binary Indexed Tree

class NumArray:
    # Segment Trees
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        # Building the segment Tree
        self.segmentTree = [0] * (4 * self.n)

        # T.C: O(2n) = O(n) cause will visit to the bottom and then add on 
        # way back up
        def buildTree(i, l, r):
            if (l == r):
                self.segmentTree[i] = nums[l]
                return
            
            mid = (l + r) // 2

            # Building the left Tree
            buildTree(2*i + 1, l, mid)
            # Building the right Tree
            buildTree(2*i + 2, mid + 1, r)

            #Storing the range sum
            self.segmentTree[i] = self.segmentTree[2*i + 1] + self.segmentTree[2*i + 2]

        buildTree(0, 0, self.n-1)

    def sumRange(self, left: int, right: int) -> int:
        def query(start, end, i, l, r):
            # condition 1: l and r is out of bounds 
            if (l > end or r < start):
                return 0
            
            # condition 2: query range is inside l and r completely 
            if (l >= start and r <= end):
                return self.segmentTree[i]
            
            # condition 3: query range is partially inside l and r 
            mid = (l + r) // 2
            # see in the left side and the right side of the node 
            return query(start, end, 2*i + 1, l, mid) + query(start, end, 2*i + 2, mid + 1, r)

        
        return query(left, right, 0, 0, self.n - 1)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)